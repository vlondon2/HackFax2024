import { Component, Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCard, MatCardActions, MatCardContent, MatCardTitle } from '@angular/material/card';
import { MatButton } from '@angular/material/button'
import { MatFormField, MatInput, MatLabel } from '@angular/material/input';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatHint} from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { UserService } from 'src/app/services/user.service';
import { MatDialog } from '@angular/material/dialog';
import { CreateAccountDialogComponent } from '../create-account-dialog/create-account-dialog.component';
import { User_Create_Response_POST, User_Get_Response_GET } from 'src/app/API types/user';
import { Router } from '@angular/router';


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
    MatCardActions,
    CreateAccountDialogComponent,
  ],
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss']
})
export class SignInComponent {

  public username;
  public password;

  constructor(@Inject(UserService) private _userService: UserService,
              @Inject(MatDialog) private _dialogService: MatDialog,
              @Inject(Router) private _router: Router)
  {
    this.username = "";
    this.password = "";
  }

  public createAccount(){

    const dialogRef = this._dialogService.open(CreateAccountDialogComponent, {
      panelClass: 'create-account-dialog',
      disableClose: true
    });

    dialogRef.afterClosed().subscribe((closingValue) => {
      if(closingValue)
      {
        this.signInNewUser(closingValue);
      }
    })
  }

  public signIn()
  {
    console.log("Username: ", this.username);
    console.log("Password: ", this.password);

    this._userService.getUser(this.username, this.password).subscribe(user => {
      
      console.log("Sign in success! ", user);
      this._userService.user = {
        id: user.id,
        username: user.username,
        level: user.level,
        cosmetics: user.cosmetics,
        xp: user.xp,
        lvlxp: user.lvlxp,
        gold: user.gold,
        tasks: user.tasks
      }
      this._loadHomePage();
    },
    error => {
      console.log("SIGN IN FAILED! ", error);
      console.log("CURRENT USER WHEN FAILURE HAPPENED: ", this._userService.user);
    })
  }

  public signInNewUser(user: User_Create_Response_POST): void {

    if(user)
    {
      this._userService.user = {
          id: user.id,
          username: user.username,
          level: 1,
          cosmetics: [],
          xp: 0,
          lvlxp: 10,
          tasks: user.tasks,
          gold: 0
      }

      this._loadHomePage();
    }
  }

  private _loadHomePage(): void{
    this._router.navigate(['/home']);
  }

}
