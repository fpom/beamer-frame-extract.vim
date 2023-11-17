import re
import vim

from pathlib import Path


_document_class = re.compile(r"^\s*\\documentclass(\[.*?\])?\{(.*?)\}")
_begin_document = re.compile(r"^\s*\\begin\{document\}")
_end_document = re.compile(r"^\s*\\end\{document\}")
_begin_frame = re.compile(r"^\s*\\begin\{frame\}")
_end_frame = re.compile(r"^\s*\\end\{frame\}")

default_frame = r"""
\begin{frame}[plain]
  \centerline{\Large{not within a frame}}
\end{frame}
"""


class Extract:
    def __call__(self):
        if vim.eval("&filetype") != "tex":
            print("not in a LaTeX file")
            return
        texpath = Path(vim.eval("expand('%:p')"))
        lineno = int(vim.eval("line('.')"))
        preamble, frame = self.split(texpath, lineno)
        if preamble is None or frame is None:
            return
        outfile = texpath.with_stem(texpath.stem + "-frame")
        outfile.write_text(preamble
                           + frame
                           + "\\end{document}\n")

    def split(self, path, lineno):
        lineno = lineno - 1
        source = tuple(path.open())
        preamble, stop = [], 0
        for lno, line in enumerate(source):
            if match := _document_class.match(line):
                if not match.group(2) == "beamer":
                    return None, None
            preamble.append(line)
            if _begin_document.match(line):
                stop = lno + 1
                break
        begin = end = None
        start = lineno
        if _end_frame.match(source[lineno]):
            start = lineno - 1
        for lno in reversed(range(stop, start+1)):
            line = source[lno]
            if _end_frame.match(line):
                break
            elif _begin_frame.match(line):
                begin = lno
                break
        start = lineno
        if _begin_frame.match(source[lineno]):
            start = lineno + 1
        for lno in range(start, len(source)):
            line = source[lno]
            if _end_document.match(line) or _begin_frame.match(line):
                break
            elif _end_frame.match(line):
                end = lno
                break
        if begin is None or end is None:
            return "".join(preamble), default_frame
        else:
            return "".join(preamble), "".join(source[begin:end+1])
