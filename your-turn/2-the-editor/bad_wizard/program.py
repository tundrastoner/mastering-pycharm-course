from game_loop import game_loop


NEWLINES_TEXT = '-----------------------------------------------------------------------'

DRAGON_TEXT = '''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
    '''


def main():
    print_header()
    game_loop()


def print_header():
    # Yes, I added this after I recorded the video
    # but I thought you'd get a kick out if it. ;)
    print()
    print(NEWLINES_TEXT)
    print(DRAGON_TEXT)
    print()
    print(NEWLINES_TEXT)
    print()


if __name__ == '__main__':
    main()
