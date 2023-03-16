import { UsersService } from './../users.service';
import { Component, OnInit } from '@angular/core';
import { Users } from '../user';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-users-list',
  templateUrl: './users-list.component.html',
  styleUrls: ['./users-list.component.css']
})
export class UsersListComponent implements OnInit {

  filterUserForm = new FormGroup({
    name: new FormControl(''),
    email: new FormControl(''),
    username: new FormControl('')
  });

  users: Users = [];
  /*variaveis utilizadas na paginação da tabela de usuarios*/
  pag: number = 1;
  counter: number = 10;

  constructor(
    private userService: UsersService,
    private formBuilder: FormBuilder,
    ){}

  ngOnInit() {
      this.userService.getUsers()
        .subscribe((data: Users) => this.users = data.map((user) => {
          return user
        }))
  }

  createForm(name: string, email: string, username: string){
    this.filterUserForm = this.formBuilder.group({
      name: name,
      username: username,
      email: email
    })
  }

  onSubmit(){
    this.getUsersFiltered(this.filterUserForm.value)
  }

  getUsersFiltered(args: any){
    this.userService.getUsersFiltered(args)
      .subscribe((data: Users) => this.users = data.map((user) => {
        /* fazendo um map no array json recebido para preencher o array de usuarios */
        return user
      }))
  }


}
