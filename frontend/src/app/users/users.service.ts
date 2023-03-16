import { Res } from './user-form/res';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { User, Users } from './user';

/* criação de variaveis para fazer as requisições */
const API_URL = environment.API_URL;
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor(private http: HttpClient) { }

  getUsers(){
    return this.http.get<Users>(`${API_URL}/users`, httpOptions)
  }

  getUsersFiltered(args: any){
    let params = new HttpParams()
      /* verificação e validação de campos Null, trocando por string vazia*/
      .set('name', args['name'] != null ? args['name'] : '')
      .set('email', args['email'] != null ? args['email'] : '')
      .set('username', args['username'] != null ? args['username'] : '')

    return this.http.get<Users>(`${API_URL}/users?${params}`, httpOptions)
  }

  createUser(user: any){
    let body = {
      'username': user.username,
      'password': user.password,
      'is_enable': user.is_enable == '1' ? true : false,
      /* ^ Conversão do formulário 0 e 1 para false ou true */
      'register_date': '',
      'name': user.name,
      'surname': user.surname,
      'email': user.email,
      'phone': user.phone,
    };

    return this.http.post<Res>(`${API_URL}/users`,body=body)

  }
}
