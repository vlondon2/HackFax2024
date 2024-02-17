import { Component, Inject } from '@angular/core';
import {MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { MatLabel, MatFormField } from '@angular/material/form-field'
import { MatButton } from '@angular/material/button';
import { MatInput } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'create-account-dialog',
  standalone: true,
  imports: [MatDialogModule, MatLabel, MatFormField, MatInput, FormsModule, MatButton],
  templateUrl: './create-account-dialog.component.html',
  styleUrl: './create-account-dialog.component.scss'
})
export class CreateAccountDialogComponent {

  get validUsernamePassword(): boolean {
    return this.username !== '' && this.password !== '' && this.confirmPassword !== '' && this.password == this.confirmPassword;
  };
  public username;
  public password;
  public confirmPassword;


  constructor(private _dialogRef: MatDialogRef<CreateAccountDialogComponent>,
              @Inject(UserService) private _userService: UserService){
    this.username = "";
    this.password = "";
    this.confirmPassword = "";
  }

  public close(): void {
    this._dialogRef.close();
  }

  public createAccount(): void{
    this._userService.createUser(this.username, this.password).subscribe((response) => {
      console.log("Successfully created the user!");
      this._dialogRef.close(response);
    },
    error => {
      console.log("Username already in use!");
    })
  }

}
