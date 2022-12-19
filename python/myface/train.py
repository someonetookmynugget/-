from torch import true_divide


class train:

    def __init__(self):
        # from facenet_pytorch import MTCNN, InceptionResnetV1
        import os
        # os.chmod("./media/photo/", 755)
        self.names =["abe","arata", "ayano","chiba","fujiwara","fukuyama","oguri","suda","takeuchi","tamaki","aragaki","ayase",
            "fukada", "hamabe", "hashimoto", "hirose", "ishihara", "nagano", "nagasawa", "toda"]
        self.abe = []
        self.ayano =[]
        self.chiba =[]
        self.fujiwara =[]
        self.fukuyama =[]
        self.arata =[]
        self.oguri = []
        self.suda = []
        self.takeuchi = []
        self.tamaki = []
        self.aragaki = []
        self.ayase = []
        self.fukada = []
        self.hamabe = []
        self.hashimoto = []
        self.ishihara = []
        self.nagano = []
        self.nagasawa = []
        self.toda = []
        self.hirose = []

#### MTCNN ResNet のモデル読み込み
        # mtcnn = MTCNN()
        # self.resnet = InceptionResnetV1(pretrained='vggface2').eval()

#### 画像ファイルから画像の特徴ベクトルを取得(ndarray 512次元)
    def feature_vector(self,image_path):
        from PIL import Image
        from facenet_pytorch import MTCNN, InceptionResnetV1
        mtcnn = MTCNN()
        resnet = InceptionResnetV1(pretrained='vggface2').eval()
        
        img = Image.open(image_path)
        img_cropped = mtcnn(img)
        feature_vector = resnet(img_cropped.unsqueeze(0))
        feature_vector_np = feature_vector.squeeze().to('cpu').detach().numpy().copy()
        return feature_vector_np

#### 2つのベクトル間のコサイン類似度を取得(cosine_similarity(a, b) = a・b / |a||b|)
    def cosine_similarity(self, a, b):
        import numpy as np
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        
        
#### 2枚の画像からそれぞれの特徴ベクトルを取得
    def loop(self, pic):
        num = 0
        import glob
        for i in range(len(self.names)): 
            for path in glob.glob(f"./media/Face2/{self.names[i]}/*.jpg"):
                num += 1
                print(num)
            # 被写体の写真path
                img1_fv = self.feature_vector(pic)
            # 芸能人の写真path
                img2_fv = self.feature_vector(path)
                similarity = float(self.cosine_similarity(img1_fv, img2_fv))
                if i == 0:
                    self.abe.append(similarity)
                elif i == 1:
                    self.arata.append(similarity)
                elif i == 2:
                    self.ayano.append(similarity)
                elif i == 3:
                    self.chiba.append(similarity)
                elif i == 4:
                    self.fujiwara.append(similarity)
                elif i == 5:
                    self.fukuyama.append(similarity)
                elif i == 6:
                    self.oguri.append(similarity)
                elif i == 7:
                    self.suda.append(similarity)
                elif i == 8:
                    self.takeuchi.append(similarity)
                elif i == 9:
                    self.tamaki.append(similarity)
                elif i == 10:
                    self.aragaki.append(similarity)
                elif i == 11:
                    self.ayase.append(similarity)
                elif i == 12:
                    self.fukada.append(similarity)
                elif i == 13:
                    self.hamabe.append(similarity)
                elif i == 14:
                    self.hashimoto.append(similarity)
                elif i == 15:
                    self.hirose.append(similarity)
                elif i == 16:
                    self.ishihara.append(similarity)
                elif i == 17:
                    self.nagano.append(similarity)
                elif i == 18:
                    self.nagasawa.append(similarity)
                else:
                    self.toda.append(similarity)
        
        result = {"阿部寛": max(self.abe), "新田真剣佑": max(self.arata), "綾野剛": max(self.ayano), "千葉雄大": max(self.chiba),
                    "藤原竜也": max(self.fujiwara), "福山雅治": max(self.fukuyama), "小栗旬": max(self.oguri),
                    "菅田将暉": max(self.suda), "竹内涼真": max(self.takeuchi), "玉木宏": max(self.tamaki), "新垣結衣": max(self.aragaki),
                    "綾瀬はるか": max(self.ayase), "深田恭子": max(self.fukada), "浜辺美波": max(self.hamabe), "橋本環奈": max(self.hashimoto),
                    "広瀬すず": max(self.hirose), "石原さとみ": max(self.ishihara), "永野芽郁": max(self.nagano), "長澤まさみ": max(self.nagasawa),
                    "戸田恵梨香": max(self.toda)}
        
        return max(zip(result.values(),result.keys()))
# (glob.glob(f"./Face2/{name}/*.jpg"))
#### 2枚の画像間の類似度を取得