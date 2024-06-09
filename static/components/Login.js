export default {
    template: `
    <form class="row g-3">
  <div class="col-auto">
  <div>{{errors}}</div>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" v-model="cred.email">
  </div>
  <div class="col-auto">
    <label for="inputPassword2" class="visually-hidden">Password</label>
    <input type="password" class="form-control" id="inputPassword2" placeholder="Password" v-model="cred.password">
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary mb-3" @click='login'>Confirm identity</button>
  </div>
</form>
    `,
    data(){
        return {
            cred:{
                "email":null,
                "password":null
            },
            errors:null
        }
    },
    methods :{
        async login(){
         const res = await fetch('/user-login',{
            method: 'POST',
            headers:{
                'Content-Type' :'application/json',

            },
            body:JSON.stringify(this.cred),
         })
         const data = await res.json()
         if(res.ok){
            localStorage.setItem('auth-token',data.token)
            this.$router.push({path:'/',query:{role:data.role}})
         }
         else{
            this.errors=data.message
         }
        }
    }
}