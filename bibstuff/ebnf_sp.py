"""
:mod:`bibstuff.ebnf_sp`: simpleparse EBNF declarations
------------------------------------------------------

Contains some simpleparse style ebnf declarations
for use in parsing with simpleparse.

:copyright: 2006 by Alan G Isaac, see AUTHORS
:license: MIT (see LICENSE)
:changes:
  20160708: disallow backtick following bracket in citeref,
    so that ``[`` is not interpreted as a citeref.
"""

# AI's modifications for reST
cites_rest = r"""
src                    := plain_or_fn_or_cite*
>plain_or_fn_or_cite<  := cite / fn_or_plain
cite                   := '[', -([]#`] / [0-9]+),-[]]+, ']_'
>fn_or_plain<          := fn / plain
fn                     := '[', ('#' / '*' / [0-9]+), ']_'
plain                  := noref_brackets / nopunct+ / punct
>nopunct<              := -punct
>punct<                :=  '[' / ']'
>noref_brackets<       := '[', -[]]+, ']', ?-'_'
"""

cites_only_rest = r"""
src                    := plain_or_fn_or_cite*
>plain_or_fn_or_cite<  := cite / fn_or_plain
cite                   := '[', -([]#`] / [0-9]+),-[]]+, ']_'
>fn_or_plain<          := fn / plain
<fn>                   := '[', ('#' / '*' / [0-9]+), ']_'
<plain>                := noref_brackets / nopunct+ / punct
>nopunct<              := -punct
>punct<                :=  '[' / ']'
>noref_brackets<       := '[', -[]]+, ']', ?-'_'
"""

#EXPERIMENTAL VERSION (use is currently recommended)
cites_xp = r"""
src                    := plain_or_known*
>plain_or_known<       := known / plain
>known<                := inline_literal / cite / fn
inline_literal         := '``', -'``'+, '``'
cite                   := '[', -([]#`] / [0-9]+),-[]]+, ']_'
fn                     := '[', ('#' / '*' / [0-9]+), ']_'
plain                  := noref_brackets / nopunct+ / punct
>nopunct<              := ?-inline_literal,-punct
>punct<                :=  '[' / ']'
>noref_brackets<       := '[', -[]]+, ']', ?-'_'
"""



# Schwilk's original:
# EBNF description of a simple text file with citations in reST format
addrefs = r'''
src                 := plain_or_cite*
>plain_or_cite<     := cite / plain
cite                := '[', -[]]+, ']_'
plain               := nocite_brackets / nopunct+ / punct
>nopunct<           := -punct
>punct<             :=  '[' / ']'
>nocite_brackets<   := '[', -[]]+, ']', ?-'_'
'''
