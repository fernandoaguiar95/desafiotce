import { UserFormComponent } from './users/user-form/user-form.component';
import { HomeComponent } from './home/home.component';
import { UsersListComponent } from './users/users-list/users-list.component';
import { UsersComponent } from './users/users.component';
import { UsersModule } from './users/users.module';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '', component: HomeComponent
  },
  {
    path: 'users',
    component: UsersComponent,
     children: [
      {
        path: '',
        component: UsersListComponent,
      },
      {
        path: 'user-form',
        component: UserFormComponent,
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
