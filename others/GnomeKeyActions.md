### Compendium of actions with zsh on GNOME Terminal
- C-a - Jump to start of the line
- C-b - Go back one character in the same line
- C-c - Cancel the current command and open a new one
- C-d - When there is no character that's been entered, it quits the terminal.
		If there are characters, works like an auto-suggest
- C-e - Go to the End of the line. Complements C-a.
- C-f - Go forward one character. Complements C-b.
- C-g - Similar to C-c
- C-h - Deletes the character behind the cursor
- C-i - When the terminal is empty(with/without leading spaces), adds a tab.
		When the last char of command is a space and the cursor is on it, shows auto suggestions
- C-j - Executes the command. Equivalent to pressing enter.
- C-k - Deletes from cursor to the end of the line.
- C-l - Clear screen
- C-m - Executes the command. Similar to C-j
- C-n - Fetches the next command in history.
- C-o - Executes the command. Similar to C-j
- C-p - Fetches the previous command in history.
- C-q - Clears current line.
- C-r - Reverse command search
- C-s - Forward command search?? 
- C-t - Swaps the last 2 characters and moves ahead by - 
		2 chars if cursor's at the start, 1 char in the middle, 0 char if at end.
- C-u - Clears current line. Similar to C-q
- C-v - None
- C-w - Clears alphanumeric chars from the chars behind the cursors till it's not alphanumeric.
- C-x - Selection of text. When cursor is at the end of the line, seems to select the entire line.
		The selection is a bit more involved when the cursor is somewhere in the middle(It keeps changing)
- C-y - Undo the clear done by C-w, C-u, (Not C-q)
- C-z - None