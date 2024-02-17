import { Component, Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCard, MatCardActions, MatCardContent, MatCardTitle } from '@angular/material/card';
import { MatButton } from '@angular/material/button'
import { MatFormField, MatInput, MatLabel } from '@angular/material/input';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatHint} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { UserService } from 'src/app/services/user.service';


@Component({
  selector: 'sign-in',
  standalone: true,
  imports: [
    MatButton,
    CommonModule, 
    MatCard, 
    MatCardTitle,
    MatCardContent, 
    MatFormField,
    MatLabel,
    MatInput, 
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    MatHint,
    MatCardActions
  ],
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss']
})
export class SignInComponent {

  constructor(@Inject(UserService) private _userService: UserService)
  {
    
  }

  public createAccount(){

    this._userService.createUser("Dom", "123").subscribe(response => {
      console.log("Response: ", response);
    },
    error => {
      console.error("Error! ", error);
    })
  }

}
