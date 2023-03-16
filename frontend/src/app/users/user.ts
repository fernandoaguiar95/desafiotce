export interface User {
  id: number,
  username: string,
  password: string,
  is_enable: boolean,
  register_date: Date,
  name: string,
  surname: string,
  email: string,
  phone: string,
}

export type Users = Array<User>
