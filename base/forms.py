from django.forms import ModelForm
from .models import Project,Message,Skill,Endorsment,Comment

class ProjectForm(ModelForm):
    class Meta:
         model = Project
         fields = ['title','thumbnail','body']

    
    def __init__(self, *args, **kwargs):
         super(ProjectForm,self).__init__(*args, **kwargs)
         self.fields['title'].widget.attrs.update(
              {'class':'form-control'}
         )

         self.fields['thumbnail'].widget.attrs.update(
              {'class':'form-control' }
         )

         self.fields['body'].widget.attrs.update(
              {'class':'form-control' }
         )


class MessageForm(ModelForm):
    class Meta:
         model = Message
         fields = ['name','email','subject','body']

    
    def __init__(self, *args, **kwargs):
         super(MessageForm,self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs.update(
              {'class':'form-control'}
         )

         self.fields['email'].widget.attrs.update(
              {'class':'form-control' }
         )
         self.fields['subject'].widget.attrs.update(
              {'class':'form-control' }
         )
         self.fields['body'].widget.attrs.update(
              {'class':'form-control' }
         )


class SkillForm(ModelForm):
    class Meta:
         model = Skill
         fields = ['title','body','logo']

    def __init__(self, *args, **kwargs):
         super(SkillForm,self).__init__(*args, **kwargs)
         self.fields['title'].widget.attrs.update(
              {'class':'form-control'}
         )

         self.fields['body'].widget.attrs.update(
              {'class':'form-control' }
         ) 
         self.fields['logo'].widget.attrs.update(
              {'class':'form-control' }
         ) 

class EndorsmentForm(ModelForm):
    class Meta:
         model = Endorsment
         fields = '__all__'
         exclude=['featured','approved']

    def __init__(self, *args, **kwargs):
         super(EndorsmentForm,self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs.update(
              {'class':'form-control'}
         )

         self.fields['body'].widget.attrs.update(
              {'class':'form-control' }
         ) 

class CommentForm(ModelForm):
     class Meta:
          model=Comment
          fields=['name','body']
          exclude=['project']
     def __init__(self, *args, **kwargs):
         super(CommentForm,self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs.update(
              {'class':'form-control'}
         )
         self.fields['body'].widget.attrs.update(
              {'class':'form-control'}
         )