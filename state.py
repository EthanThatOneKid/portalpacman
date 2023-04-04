class State:
    def __init__(self):
        self.state = None

    def toggle(self):
        if self.state is None or not self.state.is_playing:
            self.play()
        else:
            self.pause()

    def play(self):
        self.state.is_playing = True

    def pause(self):
        if self.state.is_playing != None and self.state.is_playing:
            self.state.is_playing = False
    
    def reset(self):
        self.state = None
    
    def is_main_menu(self):
        return self.state is None
    
    def is_playing(self):
        return self.state.is_playing
    
    def is_paused(self):
        return self.state.is_playing != None and not self.state.is_playing

