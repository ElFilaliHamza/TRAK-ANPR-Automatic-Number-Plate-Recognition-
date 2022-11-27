# from modules import *
import ui_anprMainUI
from ui_anprMainUI import *
from myEnv import *
class MainGui(QMainWindow):
    dataUpdated = pyqtSignal()
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = ui_anprMainUI.Ui_MainWindow()
        
        self.IMAGE_PATH = os.path.join(paths['IMAGE_PATH'], 'test', 'p1.jpg')
        self.ui.setupUi(self)
        self.show()
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray, np.ndarray, str)
    cap_input = 0
    isPlaying = True
    def run(self):
        # capture from web cam  or  r'D:\H\Work\Stage\ANPR\vid1.mp4'
        self.isPlaying = True
        cap = cv2.VideoCapture(self.cap_input)
        ret, cv_img = cap.read()
        width= cv_img.shape[1]
        height= cv_img.shape[0]
        while self.isPlaying :
            ret, cv_img = cap.read()
            if ret:
                try:
                    image_np_with_detections, boxes, scores, classes = get_detections(cv_img)
                    if boxes.any():                    
                        roi = boxes[0]*[height, width, height, width] # reagon of intreste
                        plate_img = image_np_with_detections[int(roi[0]):int(roi[2]),int(roi[1]):int(roi[3])]
                    else: 
                        setImageToView(cv_img, mainWindow.ui.video_view)
                        continue
                    plate_text = get_plate_text(plate_img)
                    
                    self.change_pixmap_signal.emit(image_np_with_detections, plate_img, plate_text)
                except EOFError as err:
                    print("get plate from frame error ========\n",err)
        cap.release()
class ImageThread(QThread):
    img_process_signal = pyqtSignal(np.ndarray, np.ndarray, str)
    img_path = None 
    def run(self):
        if self.img_path:
            try:
                image_np_with_detections, boxes, scores, classes = get_detections(self.img_path)
                if boxes.any(): 
                    width= image_np_with_detections.shape[1]
                    height= image_np_with_detections.shape[0]
                    roi = boxes[0]*[height, width, height, width] # reagon of intreste
                    plate_img = image_np_with_detections[int(roi[0]):int(roi[2]),int(roi[1]):int(roi[3])]
                    plate_text = get_plate_text(plate_img)
                    self.img_process_signal.emit(image_np_with_detections,plate_img, plate_text)
                else:
                    print('no plate detected!!')
            except RuntimeError as err:
                    print("get plate from image error ========\n",err)
class MyFileDialog(QFileDialog):
    def __init__(self):
        super().__init__()
        self.filePath = 'text'
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName = QFileDialog.getOpenFileName(
            mainWindow, "Ouvrir un fichier", "", "All Files (*);;Images (*.png)", options=options)
        if self.fileName[0]:
            mainWindow.IMAGE_PATH = self.fileName[0]
            print(self.fileName)
    

def on_load_img():
    File_Dialog.openFileNameDialog()
    img_path = File_Dialog.fileName[0]
    if validate_img_path(img_path):
        img_thread.img_path = img_path
        setImageToView(cv2.imread(img_path), mainWindow.ui.video_view)
    else:
        print('chose a valid image [png, jpg, jpeg]')
def on_start_cam():
    if not video_thread.isRunning():
        video_thread.cap_input = 0
        video_thread.start()     
        mainWindow.ui.mystatusbar.showMessage('starting camera')
def on_stop_cam():
    mainWindow.ui.mystatusbar.showMessage('stoping the camera ')
    if video_thread.isRunning():
        video_thread.isPlaying = False
        video_thread.exit()
        print("cam stoped")
        mainWindow.ui.mystatusbar.showMessage('Ready')
    
def on_load_video():
    if not video_thread.isRunning():
        mainWindow.ui.mystatusbar.showMessage('Starting video')
        File_Dialog.openFileNameDialog()
        vid_path = File_Dialog.fileName[0]
        if validate_vid_path(vid_path):
            mainWindow.ui.mystatusbar.showMessage('video started')
            video_thread.cap_input = vid_path
            video_thread.start()
def on_stop_video():
    if video_thread.isRunning():
        video_thread.isPlaying = False
        video_thread.exit()
        mainWindow.ui.mystatusbar.showMessage('video recognition stoped')
        print("vid stoped")
def on_start_recognition():
    if not img_thread.isRunning() and img_thread.img_path:
        mainWindow.ui.mystatusbar.showMessage('image recognition started')
        img_thread.start()
# def on_stop_recognition():
#     if img_thread.isRunning():
#         img_thread.exit()
#         img_thread.quit()
#         mainWindow.ui.mystatusbar.showMessage('Ready')
def on_clear_views():
    mainWindow.ui.video_view.setText('VIDEO VIEW')
    mainWindow.ui.plate_img.setText('PLATE IMAGE')
    mainWindow.ui.plate_text.setText('PLATE NUMBER')
def update_plate_views(img_with_detections, plate_img, plate_text):
    setImageToView(img_with_detections, mainWindow.ui.video_view)
    setImageToView(plate_img, mainWindow.ui.plate_img)
    mainWindow.ui.plate_text.setText(plate_text)
def setImageToView(img, view):
    try:
        w = view.width()
        h = view.height()
        view.setPixmap(convert_cv_qt(img).scaled(w,h,Qt.KeepAspectRatio))
    except:
        view.setText('Chack image formate or re run the programme')
        print('image not valid')
def validate_img_path(img_path):
    if img_path.endswith('.png'):
        return True
    if img_path.endswith('.jpg'):
        return True
    if img_path.endswith('.jpeg'):
        return True
    return False
def validate_vid_path(vid_path):
    if vid_path.endswith('.mp4'):
        return True
    if vid_path.endswith('.avi'):
        return True
    return False
def convert_cv_qt(cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
    return QPixmap.fromImage(convert_to_Qt_format)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    
    mainWindow = MainGui()
    File_Dialog = MyFileDialog()
    
    video_thread = VideoThread()
    video_thread.change_pixmap_signal.connect(update_plate_views)
    img_thread = ImageThread()
    img_thread.img_process_signal.connect(update_plate_views)
    
    mainWindow.ui.load_img_btn.clicked.connect(on_load_img)
    mainWindow.ui.open_cam_btn.clicked.connect(on_start_cam)
    mainWindow.ui.close_cam_btn.clicked.connect(on_stop_cam)
    mainWindow.ui.load_video_btn.clicked.connect(on_load_video)
    mainWindow.ui.stop_video_btn.clicked.connect(on_stop_video)
    mainWindow.ui.start_recognition_btn.clicked.connect(on_start_recognition)
    # mainWindow.ui.stop_recognition_btn.clicked.connect(on_stop_recognition)
    mainWindow.ui.clear_btn.clicked.connect(on_clear_views)
    
    
    
    # plate_text = plate_from_img(img_path)
    # print(plate_text)

    sys.exit(app.exec_())