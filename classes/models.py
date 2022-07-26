# from django.db import models


# class Course(models.Model):
#     name = models.CharField(max_length=30)


# class Lecture(models.Model):
#     name = models.CharField(max_length=30)
#     course= models.ForeignKey(Course,on_delete=models.CASCADE, related_name="courses")
#     def __str__(self):
#         return self.name



# class Slide(models.Model):
#     name = models.CharField(max_length=30)
#     link = models.URLField()
#     lectures = models.OneToOneField(Lecture,on_delete=models.CASCADE, primary_key=True,)
#     def __str__(self):
#         return self.name


# class Assignment(models.Model):
#     name = models.CharField(max_length=30)
#     link = models.URLField()
#     lec = models.OneToOneField(Lecture,on_delete=models.CASCADE, primary_key=True,)
#     def __str__(self):
#         return self.name



# class Tag(models.Model):
#     name = models.CharField(max_length=30)
#     courses =  models.ManyToManyField(Course,related_name= "tags")
#     def __str__(self):
#         return self.name


class Assignment():
    def __init__(self,name,link):
        self.name = name
        self.link = link


class Slide(Assignment):
    def __init__(self,name,link):
        super().__init__(name,link)





class Lecture(Slide):
     def __init__(self,Lec_name, name, link):
         super().__init__(name, link)
         self.Lec_name = Lec_name
         


class Tag():
	def __init__(self,tag_name):
		self.tag_name = tag_name
        
        
class Course(Tag, Lecture):
    def __init__(self,corse_name, tag_name,Lec_name):
        super().__init__(tag_name) # INH form Tag class
        super().__init__(Lec_name) # INH form Lecture class
        self.corse_name = corse_name
