import csv
import os
import pickle
import random
import sys

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import RectangleSelector
import numpy as np

def slice_selector(event):
    pass


class ImageViewer():
    def __init__(self,tensor):
        self.annotates=[]
        self.box=None

        fig=plt.figure(figsize=(20,20))
        ax1=fig.add_subplot(121)
        ax1.set_title('slice view')
        ax2=fig.add_subplot(122)
        ax2.set_title('front view')
        fig.subplots_adjust(bottom=0.25)
        self.tensor=tensor
        self.fig=fig
        self.ax1=ax1
        self.ax2=ax2
        self.set_widgets()


    def get_patient_label(self,patient_id):
        if patient_id in self.patient_label_dict.keys():
            result=str(self.patient_label_dict[patient_id])
        else:
            result="?"
        return result

    def create_key(self,patient_id):
        return "RESULT="+self.get_patient_label(patient_id)+" ID= "+str(patient_id)

    def set_widgets(self):
        #set widgets
        #x,y,x_len,y_len
        shape=self.tensor.shape
        slice_ax = self.fig.add_axes([0.25, 0.1, 0.4, 0.03])
        front_ax = self.fig.add_axes([0.25, 0.15, 0.4, 0.03])

        init_slice_index=random.randint(0,shape[0]-1)
        init_front_index=random.randint(0,shape[1]-1)

        slice_slider = Slider(slice_ax, 'slice', 0,shape[0], valinit=init_slice_index,valfmt='%d')
        front_slider = Slider(front_ax, 'front', 0, shape[1], valinit=init_front_index,valfmt='%d')
        slice_slider.on_changed(self.update_slice_image)
        front_slider.on_changed(self.update_front_image)

        self.slice_slider=slice_slider
        self.front_slider=front_slider

        self.update_slice_image(init_slice_index)
        self.update_front_image(init_front_index)

        decrease_slice_ax=self.fig.add_axes([0.75,0.1,0.1,0.04])
        decrease_slice_button=Button(decrease_slice_ax,'<')
        increase_slice_ax=self.fig.add_axes([0.85,0.1,0.1,0.04])
        increase_slice_button=Button(increase_slice_ax,'>')

        decrease_front_ax=self.fig.add_axes([0.75,0.15,0.1,0.04])
        decrease_front_button=Button(decrease_front_ax,'<')
        increase_front_ax=self.fig.add_axes([0.85,0.15,0.1,0.04])
        increase_front_button=Button(increase_front_ax,'>')

        increase_slice_button.on_clicked(self.increase_slice_index)
        decrease_slice_button.on_clicked(self.decrease_slice_index)
        increase_front_button.on_clicked(self.increase_front_index)
        decrease_front_button.on_clicked(self.decrease_front_index)

        self.increase_slice_button=increase_slice_button
        self.decrease_slice_button=decrease_slice_button
        self.increase_front_button=increase_front_button
        self.decrease_front_button=decrease_front_button

        slice_selector.RS = RectangleSelector(self.ax1, self.line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],  # don't use middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
        self.slice_selector=slice_selector

        save_ax=self.fig.add_axes([0.85,0.05,0.1,0.04])
        save_button=Button(save_ax,'save annotates')
        save_button.on_clicked(self.save_annotates)
        self.save_button=save_button

        regist_ax=self.fig.add_axes([0.75,0.05,0.1,0.04])
        regist_button=Button(regist_ax,'regist annotate')
        regist_button.on_clicked(self.regist_annotate)
        self.regist_button=regist_button

    def save_annotates(self,event):
        if self.annotates!=None:
            print("saved annotates")
            save_name='annotate_'+self.patient_id+".txt"
            with open(save_name,'w') as f:
                f.write('num,slice_idx,x_top_left,y_top_left,x_bottom_right,y_bottom_right\n')
                for idx,box in enumerate(self.annotates):
                    f.write('{},{},{},{},{},{}\n'.format(idx,box[0],box[1],box[2],box[3],box[4]))
            print("save done {}".format(save_name))
        else:
            print("no annotates exist")

    def regist_annotate(self,event):
        if self.box!=None:
            print("regist annotate {}".format(self.box))
            self.annotates.append(self.box)

    def line_select_callback(self,eclick, erelease):
        'eclick and erelease are the press and release events'
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
        print(" The button you used were: %s %s" % (eclick.button, erelease.button))
        slice_index=self.slice_slider.val
        self.box=(slice_index,x1, y1, x2, y2)

    def increase_slice_index(self,event):
        print('push inc slice')
        val=self.slice_slider.val
        self.slice_slider.set_val(min(val+1,self.tensor.shape[0]-1))

    def decrease_slice_index(self,event):
        print('push dec slice')
        val=self.slice_slider.val
        self.slice_slider.set_val(max(0,val-1))

    def increase_front_index(self,event):
        print('push inc front')
        val=self.front_slider.val
        self.front_slider.set_val(min(val+1,self.tensor.shape[1]-1))

    def decrease_front_index(self,event):
        print("push dec front")
        val=self.front_slider.val
        self.front_slider.set_val(max(0,val-1))

    def update_slice_image(self,val):
        shape=self.tensor.shape
        index=int(self.slice_slider.val)
        image=self.tensor[index]
        self.ax1.imshow(image,cmap='gray')

    def update_front_image(self,val):
        shape=self.tensor.shape
        index=int(self.front_slider.val)
        tensor_from_front=self.tensor.transpose((1,2,0))
        self.ax2.imshow(tensor_from_front[index].transpose((1,0))[::-1],cmap='gray')

def main():
    size=512
    tensor=np.array([np.arange(size**2).reshape(size,size) for i in range(100)])
    viewer=ImageViewer(tensor)
    plt.show()


if __name__ == '__main__':
    main()
