#from framework.Base.BaseElement import *
import requests
from framework.logger.logger import Logger


logger = Logger(__file__).getlog()

class API:
    def __init__(self, site):
        self.site = site

    def status(self, get):
        logger.info("Trying to get status code")
        req = requests.get(self.site + get)
        result = req.status_code
        return result

    def getJson(self, get):
        logger.info("Trying to get Json")
        req = requests.get(self.site + get)
        result = req.status_code
        try:
            json = req.json()
            return json
        except:
            return "NOT JSON!"

    def SendPOST(self, get, data):
        logger.info("Trying to send POST data")
        result = requests.post(self.site + get, data=data)
        return result

class VkApiUtils:
    def __init__(self, host, token, api_vesrion="5.52"):
        self.token = token
        self.host = host
        self.tokenKey = 'access_token'
        self.messageKey = 'message'
        self.attachments = 'attachments'
        self.server = 'server'
        self.hash = 'hash'
        self.type = 'type'
        self.post = 'post'
        self.versionKey = 'v'
        self.id = 'id'
        self.item_id = 'item_id'
        self.user_id = 'user_id'
        self.owner_id = 'owner_id'
        self.photo = 'photo'
        self.responce = 'response'
        self.post_id = 'post_id'
        self.uploadUrl = 'upload_url'
        self.version = api_vesrion
        self.wallPost = "method/wall.post"
        self.usersGet = "method/users.get"
        self.wallImageServer = "method/photos.getWallUploadServer"
        self.saveWallPhoto = "method/photos.saveWallPhoto"
        self.wallEdit = "method/wall.edit"
        self.wallComment = "method/wall.createComment"
        self.wallDelete = "method/wall.delete"
        self.getLikes = "method/likes.getList"

    def getId(self):
        logger.info("Trying to get user id")
        user_id = requests.post(self.host + self.usersGet, data={self.tokenKey: self.token,
                                                                self.versionKey: self.version}).json()
        return user_id

    def uploadImage(self, user_id, image_path):
        logger.info("Trying to upload an image")
        response = requests.post(self.host + self.wallImageServer, data={self.tokenKey: self.token,
                                                                    self.versionKey: self.version}).json()
        link = response.get(self.responce)
        url = link.get(self.uploadUrl)
        response1 = requests.post(url, files={self.photo: open(image_path, "rb")}).json()
        response2 = requests.post(self.host + self.saveWallPhoto, data={self.tokenKey: self.token,
                                                                        self.user_id: str(user_id),
                                                                        self.photo: response1.get(self.photo),
                                                                        self.server: response1.get(self.server),
                                                                        self.hash: response1.get(self.hash),
                                                                        self.versionKey: self.version}).json()
        response2 = response2.get(self.responce)[0]
        image = self.photo + str(response2[self.owner_id]) + '_' + str(response2[self.id])
        return image

    def sendPost(self, message="no message given"):
        logger.info("Trying to send post to wall with message: "+ message)
        text = requests.post(self.host + self.wallPost, data={self.tokenKey: self.token,
                                                                    self.messageKey: message,
                                                                    self.versionKey: self.version}).json()
        return text

    def postImage(self, image):
        logger.info("Trying to post an image")

        response3 = requests.post(self.host + self.wallPost, data={self.tokenKey: self.token,
                                                                   self.attachments: image,
                                                                    self.versionKey: self.version}).json()

        return response3

    def editPost(self, post_id, post_text= "", image= ""):
        logger.info("Trying to edit wall post")
        response = requests.post(self.host + self.wallEdit, data ={self.tokenKey: self.token,
                                                                   self.post_id: post_id,
                                                                   self.attachments: image,
                                                                    self.messageKey: post_text,
                                                                    self.versionKey: self.version}).json()
        return response

    def deletePost(self, post_id):
        logger.info("Trying to delete wall post")
        response = requests.post(self.host + self.wallDelete, data={self.tokenKey: self.token,
                                                                     self.post_id: post_id,
                                                                     self.versionKey: self.version}).json()
        return response

    def getPostLikes(self, post_id):
        logger.info("Trying to get all likes on wall post")
        response = requests.post(self.host + self.getLikes, data={self.tokenKey: self.token,
                                                                  self.type: self.post,
                                                                    self.item_id: post_id,
                                                                    self.versionKey: self.version}).json()
        return response

    def createComment(self, post_id, text):
        logger.info("Trying to leve a comment for post: " + post_id)
        response = requests.post(self.host + self.wallComment, data={self.tokenKey: self.token,
                                                                  self.post_id: post_id,
                                                                  self.messageKey: text,
                                                                  self.versionKey: self.version}).json()
        return response





