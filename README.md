# ascii-art
Transform image/video into ASCII art.

## Usage
Launch `py main.py` from the terminal with the necessary arguments.

### Arguments

 - `inputpath`: the path of the input video or folder contaning an image sequence
 - `resolution`: the number of times that the original resolution is going to be divided when converting to ASCII characters (default is 16)
 - `filetype`: the filetype of the frames if the input is an image sequence (default is "jpg")
 - `nameformat`: the beginning of each frame's filename if using an image sequence as input (frames' names should be \<nameformat\>frame_number.\<filetype\>) (default is "")
 - `firstframe`: the number of the first frame if the input is an image sequence (default is 0)

### Output

The result will be printed in the terminal. You may have to resize your terminal's window to get better results. I found out that on Windows, PowerShell or CMD on the Windows Terminal seem to have the best performance with the least amount of stutters.