import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User, User_Create_Response_POST, User_Get_Response_GET } from '../API types/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private _user?: User;
  get user(): User | undefined{
    return this._user;
  }
  set user(newUser: User){
    this._user = newUser;
  }

  private readonly _url: string = 'http://localhost:8000/user';
  private readonly _headers: HttpHeaders = new HttpHeaders({
    'Content-Type':'application/json'
  });

  constructor(@Inject(HttpClient) private _httpClient: HttpClient) { 
    console.log(this.user);
  }

  public createUser(username: string, password: string): Observable<User_Create_Response_POST>
  {
    return this._httpClient.post<User_Create_Response_POST>(`${this._url}/create`, { username: username, password: password }, {headers: this._headers});
  }

  public getUser(username: string, password: string): Observable<User_Get_Response_GET>
  {

    let params = new HttpParams();

    params.append('username', username);
    params.append('password', password);
    return this._httpClient.get<User_Get_Response_GET>(`${this._url}/get`, {headers: this._headers, params: params})
  }
}
