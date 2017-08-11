# Written using Python 3.6.1
# Not guaranteed to work with any other version of Python

# This script requires the HJSON package and titlecase
# You can install them both with a quick and easy `pip install hjson titlecase`

from os import path
import re
import sys

try:
    import hjson
except ImportError:
    print('No HJSON package!')
    print('Run `py -3 -m pip install hjson` on a terminal or something')
    input('(Press enter to continue) ')
    sys.exit(1)

try:
    from titlecase import titlecase
except ImportError:
    print('No titlecase package!')
    print('Run `py -3 -m pip install titlecase` on a terminal or something')
    input('(Press enter to continue) ')
    sys.exit(1)

scriptname = path.basename(sys.argv[0])

files = '''\
modifiers_template.md
'''

def md_linkify(header_text):
    return header_text.lower().translate(str.maketrans(' ', '-'))

def format_roots(source):
    # [TODO] Warn if CV value is the same as another root or might conflict with a modifier
    return '[TODO]\n'

def format_modifiers(source):
    with open(source) as f:
        contents = ''
        real_output = '\n'
        def handle_key_error(*args):
            print("WARNING: missing `{}` value on '{}' in '{}' modifiers list".format(*args))
        for category_name, modifiers in hjson.loads(f.read()).items():
            contents += '* [{}](#{})\n'.format(titlecase(category_name), md_linkify(category_name))
            real_output += '## {0}\n\n'.format(titlecase(category_name))
            for abbreviation, data in modifiers.items():
                try:
                    try:
                        output = '### `{}` {}\n\n'.format(abbreviation.upper(), titlecase(data['g']))
                    except KeyError:
                        handle_key_error('g', abbreviation, category_name)
                        raise
                    try:
                        # [TODO] Warn if consonantal value is the same as a case modifier
                        # [TODO] Warn if consonantal value conflicts with another modifier
                        output += 'Cm value: **{}**  \n'.format(data['c'])
                    except KeyError:
                        handle_key_error('c', abbreviation, category_name)
                        raise
                    # [TODO] Probably deprecate?
                    output += 'CVr value: **{}**\n\n'.format(data['cv'] if 'cv' in data else data['c'] + 'e')
                    try:
                        for i in range(9):
                            output += '{}. {}\n'.format(str(i + 1), data['d'][i])
                    except KeyError:
                        print("Error: not all degrees are present for '{}' in '{}' modifiers list".format(abbreviation, category_name))
                        raise
                    output += '\n'
                    if 'n' in data:
                        output += data['n'] + '\n\n'
                    if 'src' in data:
                        output += 'This modifier is based on the `{}` suffix from Ithkuil 2011.\n\n'.format(data['src'].upper())
                    contents += '  * [`{}` {}](#{})\n'.format(abbreviation.upper(), titlecase(data['g']),
                                                             md_linkify(abbreviation + ' ' + data['g']))
                    real_output += output
                except KeyError:
                    pass
    return contents + real_output[:-1] # trim one trailing newline


for filename in files.splitlines():
    with open(filename, 'r') as f:
        output = ''
        outfile = None
        for line in f:
            match = re.match(r'~~([^\s]*)(\s+(.*))?\n', line)
            if match is None:
                output += line
            elif match.group(1) == '':
                pass
            elif match.group(1) == 'OUTFILE':
                outfile = match.group(3)
            elif match.group(1) == 'AUTOGEN_WARNING':
                output += '_This file was automatically generated by `{0}`. Do not make changes to this file directly; instead modify {1}._\n'.format(scriptname, match.group(3))
            elif match.group(1) == 'ROOTSLIST':
                output += format_roots(match.group(3))
            elif match.group(1) == 'MODIFIERSLIST':
                output += format_modifiers(match.group(3))
        if outfile is None:
            print('WARNING: No OUTFILE for {0}!'.format(filename))
        else:
            with open(outfile, 'w') as f:
                f.write(output)
