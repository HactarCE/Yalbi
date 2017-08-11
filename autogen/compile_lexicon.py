# Written using Python 3.6.1
# Not guaranteed to work with any other version of Python

# This script requires the HJSON package and titlecase
# You can install them both with a quick and easy `pip install hjson titlecase`

from collections import OrderedDict
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
roots_template.md
modifiers_template.md
'''

def md_linkify(header_text):
    return header_text.lower().translate(str.maketrans(' ', '-', '!"#$%&\'()*+,./:;<=>?@[\]^`{|}~')) # replace space with dash and remove all chars other than a-z, A-Z, 0-9, dash, and underscore

def format_roots(source):
    # [TODO] Warn if CV value is the same as another root or might conflict with a modifier
    with open(source) as f:
        contents = ''
        real_output = '\n'
        for category_name, roots in hjson.loads(f.read()).items():
            contents += '* [{}](#{})\n'.format(titlecase(category_name), md_linkify(category_name))
            real_output += '## {}\n\n'.format(titlecase(category_name))
            for root, data in roots.items():
                if root.startswith('@'):
                    continue
                try:
                    definition = data['d'] if isinstance(data['d'], str) else data['d'][0]
                    if isinstance(data['s'], OrderedDict):
                        stems = ''
                        for stem, meaning in data['s'].items():
                            if not stem.startswith('_'):
                                stems += '\n**{}** - {}  '.format(stem, meaning)
                        if stems:
                            stems = stems[1:-2] + '\n'
                    else:
                        if data['s'] == root:
                            stems = ''
                            for stem, meaning in roots['@' + root]['s'].items():
                                if not stem.startswith('_'):
                                    if 'a@' in meaning and (not isinstance(data['d'], str) or len(data['d'] < 2)):
                                        print("WARNING: no dictionary article ('a' or 'an') for '{}' in '{}' roots list".format(root, category_name))
                                        raise Exception('continue')
                                    stems += '\n**{}** - {}  '.format(stem, meaning[0].replace('a@', data['d'][1] + '@').replace('@', definition))
                            if stems:
                                stems = stems[1:-2] + '\n'
                        else:
                            try:
                                d = roots[data['s']]['d']
                                link_to_pattern = md_linkify('-{}- {}'.format(data['s'][0][1:], d if isinstance(d, str) else d[0]))
                                stems = 'This root is patterned after the root [-{}-](#{}).\n'.format(data['s'].upper(), link_to_pattern)
                            except KeyError:
                                print("WARNING: unable to find pattern for '{}' in '{}' roots list".format(root, category_name))
                                continue
                    output = "##### -{}- '{}'\n\n{}\n".format(root.upper(), definition.upper(), stems)
                    if 'src' in data:
                        output += "This root is based on -{}- from [Ithkuil 2011](http://www.ithkuil.net/lexicon.htm).\n\n".format(data['src'].upper())
                    if data['s'] == root and 'n' in roots['@' + root]:
                        output += roots['@' + root]['n'] + '\n\n'
                    if 'n' in data:
                        output += data['n'] + '\n\n'
                    contents += "  * [-{}- '{}'](#{})\n".format(root.upper(), definition.upper(), md_linkify('-{}- {}'.format(root, definition)))
                    real_output += output
                except KeyError as e:
                    print("WARNING: missing `{}` value on '{}' in '{}' roots list".format(e.args[0], root, category_name))
                except Exception as e:
                    if not e.args[0] == 'continue':
                        raise
    return contents + real_output[:-1]

def format_modifiers(source):
    with open(source) as f:
        contents = ''
        real_output = '\n'
        for category_name, modifiers in hjson.loads(f.read()).items():
            contents += '* [{}](#{})\n'.format(titlecase(category_name), md_linkify(category_name))
            real_output += '## {}\n\n'.format(titlecase(category_name))
            for abbreviation, data in modifiers.items():
                try:
                    output = '### `{}` {}\n\n'.format(abbreviation.upper(), titlecase(data['g']))
                    # [TODO] Warn if consonantal value is the same as a case modifier
                    # [TODO] Warn if consonantal value conflicts with another modifier
                    output += 'Cm value: **{}**  \n'.format(data['c'])
                    # [TODO] Probably deprecate?
                    output += 'CVr value: **{}**\n\n'.format(data['cv'] if 'cv' in data else data['c'] + 'e')
                    for i in range(9):
                        output += '{}. {}\n'.format(str(i + 1), data['d'][i])
                    output += '\n'
                    if 'src' in data:
                        output += 'This modifier is based on the `{}` suffix from [Ithkuil 2011](http://www.ithkuil.net/07_suffixes.htm).\n\n'.format(data['src'].upper())
                    if 'n' in data:
                        output += data['n'] + '\n\n'
                    contents += '  * [`{}` {}](#{})\n'.format(abbreviation.upper(), titlecase(data['g']),
                                                             md_linkify(abbreviation + ' ' + data['g']))
                    real_output += output
                except KeyError as e:
                    print("WARNING: missing `{}` value on '{}' in '{}' modifiers list".format(e.args[0], abbreviation, category_name))
                except IndexError:
                    print("WARNING: not all degrees are present for '{}' in '{}' modifiers list".format(abbreviation, category_name))
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
                output += '_This file was automatically generated by [`{0}`](autogen/{0}). Do not make changes to this file directly; instead modify {1}._\n'.format(scriptname, match.group(3))
            elif match.group(1) == 'ROOTSLIST':
                output += format_roots(match.group(3))
            elif match.group(1) == 'MODIFIERSLIST':
                output += format_modifiers(match.group(3))
        if outfile is None:
            print('WARNING: No OUTFILE for {0}!'.format(filename))
        else:
            with open(outfile, 'w') as f:
                f.write(output)
