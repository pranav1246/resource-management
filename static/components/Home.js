import StudentHome from "./StudentHome.js"
import AdminHome from "./AdminHome.js"
import InstructorHome from "./InstructorHome.js"

export default {
    template: `<div>
    <StudentHome v-if="userRole==='stud'"/>
    <AdminHome v-if="userRole==='admin'"/>
    <InstructorHome v-if="userRole==='inst'"/>
    </div>`,
    data(){
        return{
            userRole:this.$route.query.role,
        }
    },
    components:{
        StudentHome,
        InstructorHome,
        AdminHome
    }
}