import gtk,webkit

def go(widget):
	addr = addressbar,get_text()
	if not add.startswith("http://") or add.startswith("https://"):
		add = "http://" + add
		addressbar.set_text = add

	web.open(add)

win=gtk.window()
win.connect('destroy',lambda w: gtk.main_quit())

W1 = gtk.VBox()   #window 1
win.add(W1)      #adding W1 to display

box2 = gtk.HBox()
W1.pack_start(box2,False)

addressbar = gtk.Entry() #entry text box
box2.pack_start(addressbar)

gobutton = gtk.Button("GO")
box2.pack_start(gobutton)
gobutton.connect('clicked',go)

scroller = gtk.ScrolledWindow()
box1.pack_start(scroller)

web = webkit.WebView()
scroller.add(web)


win.show_all
gtk.main()


