import { MatDrawer, MatDrawerContainer, MatDrawerContent } from '@angular/material/sidenav';
import { NavigationComponent } from 'src/app/components/navigation/navigation.component';
import { MatButtonModule } from '@angular/material/button';
import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { UserService } from 'src/app/services/user.service';
import { Achievement, User } from 'src/app/API types/user';


@Component({
  selector: 'achievement-list',
  standalone: true,
  imports: [MatIcon, MatDrawer, MatDrawerContainer, MatDrawerContent, NavigationComponent, MatButtonModule],
  templateUrl: './achievement-list.component.html',
  styleUrl: './achievement-list.component.scss'
})
export class AchievementListComponent implements OnInit{
  @ViewChild('drawer') public drawer?: MatDrawer;
  public user?: User;
  public achievements: Achievement[];

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
    this.achievements = [];
 
  }

  public ngOnInit(): void
  {
    if(this.user)
    {
      this._userService.getAchievements(this.user.id).subscribe(response => {
        this.achievements = response.achievements;
        console.log(response);
      })
    }
  }

 
  public toggleNav(): void {
    this.drawer?.toggle();
  }

}
