# `vim` plugin to extract the beamer frame under the cursor

This `vim` plugin adds a command for LaTeX files to extracts the beamer frame that is under the cursor.
If editing file `spam.tex`, the extracted frame is saved to `spam-frame.tex` that includes:

 * the full preamble from `spam.tex`
 * the source code of the current frame
 * `\end{document}`

If the cursor is currently not within a frame, a dummy frame is saved instead.

Note that LaTeX source code is extracted from the saved file and not from the live buffer in order to rely on a content whose consistency is under user's control.
Note also that the plugin expects `\begin{frame}`, `\end{frame}`, `\begin{document}`, and `\end{document}` to be written at the beginning of lines without anything before except possible spaces.

Automation can be performed by asking `vim` to run the command every time the file is saved:

```
autocmd BufWritePost,FileWritePost *.tex :BeamerFrameExtract
```

Then, launch `latexmk spam-frame` or other automated compiler to get an up-to-date PDF of the frame currently edited.
The plugin does not take care of compilation, it just extract and save the relevant source code.

## Dependencies

The plugin requires `python3` to be available in `vim`.

## Licence

`beamer-frame-extract` is (C) 2023 Franck Pommereau <franck.pommereau@univ-evry.fr> and released under the terms of MIT licence, see file `LICENCE` for details.
