from django.db import models

# Create your models here.
class Questions(models.Model):
    text=models.CharField(max_length=50,null=True,blank=True)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"{self.text}"

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): 
        return f"{self.question.text} ->{self.choice_text}"