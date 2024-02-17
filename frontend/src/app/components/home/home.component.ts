import { Component, Inject, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService } from 'src/app/services/user.service';
import { User } from 'src/app/API types/user';''
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatDrawer, MatSidenavModule} from '@angular/material/sidenav';
import { MatIconButton } from '@angular/material/button';
import { MatIcon } from '@angular/material/icon';
import { NavigationComponent } from '../navigation/navigation.component';

@Component({
  selector: 'home',
  standalone: true,
  imports: [CommonModule, NavigationComponent, MatButtonModule, MatSelectModule, MatFormFieldModule, MatSidenavModule, MatIconButton, MatIcon],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  public user?: User;

  @ViewChild('drawer') public drawer?: MatDrawer;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
  }

  public getTree(): string{
    let src = '';
    switch(this.user?.level)
    {
      case 1:
        src='assets/TreeSaplingAndLand.png'
        break;
      case 2:
        src='assets/MediumTree.png'
        break;
      case 3:
        src='assets/FullTreeAndLandImage.png'
        break;
    }

    return src;
  }

  public getUsername(): string {
    if(this.user)
    {
      return this.user.username;
    }

    return "Undefined";
  }

  public toggleNav(): void {
    console.log("Calling toggleNav!");
    this.drawer?.toggle();
  }

  public getUserXPBarStyle() {
    if(this.user)
    {
      let xpPercentage = (this.user.xp / this.user.lvlxp) * 100;

      return {
        width: `${xpPercentage}%`
      }
    }

    return{
      width: '0%'
    }
  }

}
