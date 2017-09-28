/*
 *  USAGE INSTRUCTIONS
 *  Ctrl + Win + semicolon  Exit
 *  Win + semicolon         ə ŋ
 *
 *  Type using the normal orthography, but press Win + semicolon instead of
 *  period. This script will not work in some programs, such as Google Chrome
 *  unless it is run with administrator privelages.
 */

#InstallKeybdHook
#NoEnv
#SingleInstance Force
SendMode Input

SoundBeep, 1046.502, 100
SoundBeep, 1567.982, 100

inputMode := 0

typeChar(char) {
  If (GetKeyState("CapsLock", "T") ^ GetKeyState("Shift"))
    StringUpper char, char
  Global inputMode := 0
  ToolTip
  Send %char%
}

Return ; END OF AUTO-EXECUTE SECTION

^#;::
SoundBeep, 391.996, 100
SoundBeep, 261.626, 100
ExitApp

#;::
inputMode := 1
ToolTip ə ŋ
Return

#If inputMode
Esc::
inputMode := 0
ToolTip
Return

*e::typeChar("ə")
*n::typeChar("ŋ")
