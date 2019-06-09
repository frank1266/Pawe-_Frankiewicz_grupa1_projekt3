from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import shuffle
global points, counts
#from math import sin, cos, acos, pi



points = [
        ['paris.jpg', 48.858347  , 2.29455],
        ['waw.jpg', 52.239366, 21.045784],
        ['koloseum.jpg', 41.89, 12.492222],
        ['stone.jpg', 51.178844, -1.826189],
        ['pomnik.jpg', -22.951389, -43.210833],
        ['skala.jpg', -25.345, 131.036111],
        ['szwecja.jpg', 55.613333, 12.976389],
        ['anfield.jpg', 53.430864, -2.960692],
        ['tower.jpg', 51.508056, -0.076111],
        ['zydeum.jpg', 52.249444, 20.992778],
        ]
shuffle(points)
counts=len(points)
class Form(BoxLayout):   
    def draw_marker(self):
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{:.5f}".format(self.latitude)
        self.search_long.text = "{:.5f}".format(self.longitude)
        
    def check_points(self):
        r=3
        #R=6371000
        if self.my_image.source in ['hello1.gif','meta.jpg']:
            pass
        else:
            if (self.latitude-self.curr_img[1])**2 + (self.longitude -self.curr_img[2])**2 <= r**2:
                #R*(acos(cos((pi/2)-self.latitude)*cos((pi/2)-self.curr_img[1])+sin((pi/2)-self.latitude)*sin((pi/2)-self.curr_img[1])*cos(self.curr_img[2]-self.longitude)))<=2000000
                self.my_score.text=str(int(self.my_score.text)+1)
                self.my_button_check.disabled = True
            else:
                self.my_button_check.disabled = True
        
            
        
                
    def next_img(self):
        self.my_button_check.disabled = False
        if len(points)>=1:
            self.curr_img=points.pop()
            self.my_image.source = self.curr_img[0]
            self.my_button_next.text='NEXT'
        else:
            self.my_image.source = 'meta.jpg'
            self.my_button_next.disabled = True
            self.my_button_check.disabled = True
            self.my_button_next.text='QUIZ SKOŃCZONY'
    
    
        


class MapViewApp(App):
    pass

MapViewApp().run()