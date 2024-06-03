from flask_restful import Resource, Api, reqparse , marshal_with, fields
from .models import StudyResource ,db

api = Api(prefix='/api')

# request parser  middleware

parser = reqparse.RequestParser()
parser.add_argument('topic', type=str, help='topic should be a string' ,required=True)
parser.add_argument('description', type=str, help='descritiption should be a string',required=True)
parser.add_argument('resource_link', type=str, help='link should be a string',required=True)

# structure the resource data as required to be sent
study_resource_fields={
    'id':fields.Integer,
    'topic':fields.String,
    'description':fields.String,
    'resource_link':fields.String
}
class StudyMaterial(Resource):
    @marshal_with(study_resource_fields)
    def get(self):
        all_study_material=StudyResource.query.all()
        if len(all_study_material)>0:
            return {"message":"No resourece found"},404
        return all_study_material

    def post(self):
        args = parser.parse_args()
        study_resource=StudyResource(**args)
        db.session.add(study_resource)
        db.session.commit()
        return {"message":"created"}


api.add_resource(StudyMaterial, '/study_material')

