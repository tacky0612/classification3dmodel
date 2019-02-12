# encoding: utf-8
import os
import keras
from keras.optimizers import Adam
from keras.callbacks import LearningRateScheduler, ModelCheckpoint , TensorBoard

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config():
    
    def make_tensorboard(set_dir_name='TensorBoard'):
        log_dir = set_dir_name
        if os.path.exists(log_dir) == False:
            os.makedirs(log_dir)
        tensorboard = TensorBoard(log_dir=log_dir, write_graph=True, )
        return tensorboard
    
#     DATASET = "ModelNet10"
#     DATASET = "ModelNet40"
    DATASET = "3D_SAMPLE"
    
    
    N_POINTS = 10000
    CELL = 32
    BATCH_SIZE = 128
    EPOCHS = 40
    LEARNIG_RATE = 0.001
    
    
    OPTIMIZER = Adam(lr=LEARNIG_RATE)
   
    
    if DATASET == "ModelNet10":
        DATA_DIR = "ModelNet10/"
        NUM_CLASSES = 10
        EXTENSION = ".off"
        CLASS_NAME = [
        'bathtub',
        'chair',
        'dresser',
        'night_stand',
        'table',
        'bed',
        'desk',
        'monitor',
        'sofa',
        'toilet',
        ]
        
    if DATASET == "ModelNet40":
        DATA_DIR = "ModelNet40/"
        NUM_CLASSES = 40
        EXTENSION = ".off"
        CLASS_NAME = [
        'airplane',
        'bookshelf',
        'chair',
        'desk',
        'glass_box',
        'laptop',
        'person',
        'range_hood',
        'stool',
        'tv_stand',
        'bathtub',
        'bottle',
        'cone',
        'door',
        'guitar',
        'mantel',
        'piano',
        'sink',
        'table',
        'vase',
        'bed',
        'bowl',
        'cup',
        'dresser',
        'keyboard',
        'monitor',
        'plant',
        'sofa',
        'tent',
        'wardrobe',
        'bench',
        'car',
        'curtain',
        'flower_pot',
        'lamp',
        'night_stand',
        'radio',
        'stairs',
        'toilet',
        'xbox',
        ]
    
    if DATASET == "3D_SAMPLE":
        DATA_DIR = "3D_SAMPLE/"
        NUM_CLASSES = 34
        EXTENSION = ".stl"
        CLASS_NAME = [
        'auto_valve1',
        'auto_valve2',
        'auto_valve3',
        'bearing',
        'bevel_gear',
        'block',
        'bracket1',
        'bracket2',
        'bushing',
        'cylinder',
        'etc',
        'frame',
        'gear',
        'handle_valve1',
        'handle_valve2',
        'handle_valve3',
        'hinge1',
        'hinge2',
        'nut',
        'pipe',
        'plate',
        'pully1',
        'pully2',
        'robot1',
        'robot2',
        'robot3',
        'robot4',
        'rod',
        'shaft1',
        'shaft2',
        'spring',
        'trigeminal_valve',
        'valve_connector',
        'washer'
        ]
        
        
    VOX_DIR = "np_vox/" + DATASET + "/cell" + str(CELL) + "/"
    FIG_DIR =  "figure/"+ DATASET + "/cell" + str(CELL) + "/"
    WEIGHTS_DIR = "weights/" + DATASET + "/cell" + str(CELL) + "/"
    MODEL_DIR = "model/"+ DATASET + "/cell" + str(CELL) + "/"
    DIST_DIR = "dist/"+ DATASET + "/cell" + str(CELL) + "/"
    
    # early_stopping
    early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=0, verbose=0, mode='auto')
    
    #save best model
    checkpoint = ModelCheckpoint(filepath = os.path.join(WEIGHTS_DIR, "model-{epoch:02d}.h5"), save_best_only=True)
    
    # TensorBoard
    CALLBACKS = [make_tensorboard(),checkpoint]
    
    
    
    
config = Config()


