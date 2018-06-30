def getch():
    #Returns a single character from standard input
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:                                                                                            
        tty.setraw(sys.stdin.fileno())                                                              
        ch = sys.stdin.read(1)                                                                      
    finally:                                                                                                                                
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)                                                                              
    return ch
