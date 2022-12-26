from rest_framework import serializers
from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()
    
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only  yazdığımız metodu serialize edecek başına get konulur  def get_born_year(self, obj):   böylece born_year aşağıda fieldler arasına yazılabildi
    path = serializers.StringRelatedField() # read_only     path jangoda karışıyor bize id getiriyor bizde path modülündeki str kısmını al dedik
    path_id = serializers.IntegerField() #biz modelde path seçsekte veritabanına path_id olarak kaydetmiş çağırırken path şeklinde yazarsak path_id yi çağırıyor yukarıda
    # bu karışıklığı düzelttik  ayrıyeten path_id yi de görmek istiyoruz aşağıda path_id yi yazdık artık çağırrıken problem yok ama post işlemlerinde serializers olmayacak 
    # bu seferde path_id yi serialize ettik.
    class Meta:
        model = Student
        # fields = "__all__"
        # fields = ["id","first_name", "last_name","number", "age", "born_year", "path", "path_id"]
        exclude = []  # hiçbirşeyi hariç tutma dedik all ile aynı mantık
        
    
    def get_born_year(self, obj):   #burada  SerializerMethodField   metodu obje olarak datanın hepsini almış  içinden age yi seçtik
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
    
class PathSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True)
    students = serializers.HyperlinkedRelatedField(  #link şeklinde verildi
        many=True,
        read_only=True,
        view_name='detail'
    )
    
    # students = StudentSerializer(many=True) sadece data çağırır
    
    class Meta:
        model = Path
        # fields = "__all__"
        fields = ["id", "path_name", "students"]    # buradaki student relation_name olark tanımlandı o radan çağırdık 