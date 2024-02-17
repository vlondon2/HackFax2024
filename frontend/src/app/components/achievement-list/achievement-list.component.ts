import { MatDrawer, MatDrawerContainer, MatDrawerContent } from '@angular/material/sidenav';
import { NavigationComponent } from 'src/app/components/navigation/navigation.component';
import { MatButtonModule } from '@angular/material/button';
import { Component, Inject, ViewChild } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { UserService } from 'src/app/services/user.service';
import { User } from 'src/app/API types/user';


@Component({
  selector: 'achievement-list',
  standalone: true,
  imports: [MatIcon, MatDrawer, MatDrawerContainer, MatDrawerContent, NavigationComponent, MatButtonModule],
  templateUrl: './achievement-list.component.html',
  styleUrl: './achievement-list.component.scss'
})
export class AchievementListComponent {
  @ViewChild('drawer') public drawer?: MatDrawer;
  public user?: User;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
 
  }

  public ngOnInit(): void {
    
  }
  public toggleNav(): void {
    this.drawer?.toggle();
  }

}
