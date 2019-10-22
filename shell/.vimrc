"set nocom9
"source $VIMRUNTIME/vimrc_example.vim
set ignorecase
"set colorcolumn=80
"set tags=/local/lingkong/sf_lte/tags

"set window size
"set lines=46 columns=110
set columns=100
"set lines=40
set guifont=Monospace\ Bold\ 13
"set guifont=Monospace\ 10
"set guifont=Bitstream\ Vera\ Sans\ Mono\ 10
"set autoindent
"set smartindent
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set nu
set ruler
set laststatus=2
set statusline=[%F]%y%r%m%*%=[Line:%l/%L,Column:%c][%p%%]
set showmatch
set showcmd
set showfulltag
set showmode
set smartcase
set imcmdline
set nowrap
set cursorline
set bsdir=buffer
"set autochdir
set backspace=indent,eol,start
"set mouse=a
set guioptions-=T
set splitbelow
set splitright


" no backup files and swap files will be created -begin
set nobackup 
set nowritebackup
set noswapfile
" no backup files and swap files will be created -end

set previewwindow
"set wrap
set guitablabel=%N/\ %t\ %M
set hlsearch
set incsearch
set expandtab
syntax enable
syntax on
autocmd BufReadPost * if line("'\"") && line("'\"") <= line("$") | exe "normal `\"" | endif
"set background=dark
"colorscheme evening
colorscheme molokai
map <C-t> :tabedit ./

let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1

let Tlist_Auto_Open=1
let Tlist_Auto_Open=1
"source Session.vim


""set indent guide settings
"let g:indent_guides_enable_on_vim_startup = 1
"let g:indent_guides_auto_colors = 0
"let g:indent_guides_guide_size = 1
"
"autocmd VimEnter, Colorscheme *:hi IndentGuidesOdd  guibg=red   ctermbg=3
"autocmd VimEnter, Colorscheme *:hi IndentGuidesEven guibg=green ctermbg=4
"
"hi IndentGuidesOdd  guibg=red   ctermbg=3
"hi IndentGuidesEven guibg=green ctermbg=4
""end of Indent guides setting

source ~/cscope_maps.vim

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction

map ,ch :call SetColorColumn()<CR>
function! SetColorColumn()
    let col_num = virtcol(".")
    let cc_list = split(&cc, ',')
    if count(cc_list, string(col_num)) <= 0
        execute "set cc+=".col_num
    else
        execute "set cc-=".col_num
    endif
endfunction
