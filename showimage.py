from gi.repository import Gtk
import cairo


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        self.load_image()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Image")
        self.resize(400, 400)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
        
    def load_image(self):
        
        self.ims = cairo.ImageSurface.create_from_png("8-1.png")
        
            
    def on_draw(self, wid, cr):

        cr.set_source_surface(self.ims, 10, 10)
        cr.paint()
        
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
