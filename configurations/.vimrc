" Set the background color to dark
set background=dark

" Set the color scheme to dracula
colorscheme dracula

" Enable syntax highlighting
syntax on

" Show absolute line numbers
set number

" Show relative line numbers
set relativenumber

""" Map leader to space ---------------------
let mapleader=" "

" Map Ctrl-C to act as Esc in normal mode
nnoremap <C-c> <Esc>

" Map Ctrl-C to act as Esc in insert mode
inoremap <C-c> <Esc>

" Map Ctrl-C to act as Esc in visual mode
vnoremap <C-c> <Esc>

" Center the screen after jumping to the next search result
nnoremap n nzzzv

" Center the screen after jumping to the previous search result
nnoremap N Nzzzv

" Paste over a visual selection without yanking the replaced text
xnoremap <leader>p "_dP

