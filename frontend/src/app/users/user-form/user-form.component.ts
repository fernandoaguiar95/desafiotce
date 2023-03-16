import { Router } from '@angular/router';
import { Res } from './res';
import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { UsersService } from '../users.service';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {

  data: any;

  userForm = new FormGroup({
    name: new FormControl(''),
    email: new FormControl(''),
    password: new FormControl(''),
    is_enable: new FormControl(''),
    username: new FormControl(''),
    surname: new FormControl(''),
    phone: new FormControl(''),
  });

  ngOnInit(): void {
  }

  constructor(
    private userService: UsersService,
    private router: Router,
    ){}

  onSubmit(){
    this.createUser(this.userForm.value)
  }

  createUser(user: any){
    if(this.userForm.valid){
      this.userService.createUser(user)
      .subscribe(data => {
        if(data.status == true){
          this.router.navigate(['users'])
        } else {
          alert(data.message)
        }
      });
    } else {
      alert('Campos inválidos!')
    }
  }

}
