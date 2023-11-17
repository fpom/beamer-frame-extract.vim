" beamer-frame-extract: Extract the beamer frame under the cursor
"
" Script Info  {{{
"=============================================================================
"      Licence: The MIT Licence (see LICENCE file)
" Name Of File: beamer_frame_extract.vim
"  Description: Extract the beamer frame under the cursor
"   Maintainer: Franck Pommereau <franck.pommereau@univ-evry.fr>
"      Version: 0.0.2
"        Usage: Use :help  for information on how to configure and use
"               this script, or visit the Github page
"               <https://github.com/fpom/beamer-frame-extract.vim>
"
"=============================================================================
" }}}

" Do not source this script when python is not compiled in.
if !has('python3')
    echomsg ':python3 is not available, beamer-frame-extract will not be loaded.'
    finish
endif

python3 import beamer_frame_extract
python3 bfextract = beamer_frame_extract.Extract()

command! BeamerFrameExtract python3 bfextract()
