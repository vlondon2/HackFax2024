import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User_Create_Response_POST } from '../API types/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private readonly _url: string = 'http://localhost:8000/user';
  private readonly _headers: HttpHeaders = new HttpHeaders({
    'Content-Type':'application/json'
  });

  constructor(@Inject(HttpClient) private _httpClient: HttpClient) { 

  }

  public createUser(username: string, password: string): Observable<User_Create_Response_POST>
  {
    return this._httpClient.post<User_Create_Response_POST>(`${this._url}/create`, { username: username, password: password }, {headers: this._headers});
  }
}
