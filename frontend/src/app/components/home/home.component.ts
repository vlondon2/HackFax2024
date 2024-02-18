import { Component, Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService } from 'src/app/services/user.service';
import { User } from 'src/app/API types/user';

@Component({
  selector: 'home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  public user?: User;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
  }

  public getTree(): string{
    let src = '';
    switch(this.user?.level)
    {
      case 1:
        src='assets/'
        
    }
  }


}
