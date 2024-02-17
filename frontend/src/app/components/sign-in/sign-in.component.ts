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
import { User_Create_Response_POST } from 'src/app/API types/user';


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
    CreateAccountDialogComponent
  ],
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.scss']
})
export class SignInComponent {

  constructor(@Inject(UserService) private _userService: UserService,
              @Inject(MatDialog) private _dialogService: MatDialog)
  {
  }

  public createAccount(){

    const dialogRef = this._dialogService.open(CreateAccountDialogComponent, {
      panelClass: 'create-account-dialog',
      disableClose: true
    });

    dialogRef.afterClosed().subscribe((closingValue) => {
      if(closingValue)
      {
        this.signIn(closingValue);
      }
    })
  }

  public signIn(user: User_Create_Response_POST): void {

    if(user)
    {
      this._userService.user = {
          id: user.id,
          username: user.username,
          level: 1,
          cosmetics: [],
          xp: 0,
          lvlxp: 10,
          tasks: [],
          gold: 0
      }

    }
  }

}
