class SceneManager:
    def __init__(self, main_menu_scene, playing_scene, paused_scene):
        self.state = None
        self.main_menu_scene = main_menu_scene
        self.playing_scene = playing_scene
        self.paused_scene = paused_scene

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

    def update_current_scene(self):
        if self.is_main_menu():
            self.main_menu_scene.update()
        elif self.is_playing():
            self.playing_scene.update()
        elif self.is_paused():
            self.paused_scene.update()

    def draw_current_scene(self):
        if self.is_main_menu():
            self.main_menu_scene.draw()
        elif self.is_playing():
            self.playing_scene.draw()
        elif self.is_paused():
            self.paused_scene.draw()
