import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { MatDrawer, MatDrawerContainer, MatDrawerContent } from '@angular/material/sidenav';
import { NavigationComponent } from 'src/app/components/navigation/navigation.component';
import { Task, User } from 'src/app/API types/user';
import { UserService } from 'src/app/services/user.service';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-task-board',
  standalone: true,
  imports: [MatIcon, MatDrawer, MatDrawerContainer, MatDrawerContent, NavigationComponent, MatButtonModule],
  templateUrl: './task-board.component.html',
  styleUrl: './task-board.component.scss'
})
export class TaskBoardComponent implements OnInit{

  @ViewChild('drawer') public drawer?: MatDrawer;
  public user?: User;
  public tasks: Task[];
  constructor(@Inject(UserService) private _userService: UserService){
    this.user = this._userService.user;
    this.tasks = [];
    //this.tasks = [{name: "Recycle", description: "Place long ass description that will get cut off hopefully some plastic or other recycable materials in the recycling bin.", xp: 3}, {name: "Recycle", description: "Description", xp: 3}, {name: "Recycle", description: "Description", xp: 3}, {name: "Recycle", description: "Description", xp: 3}];
  }

  public ngOnInit(): void {
    if(this.user)
    {
      this.tasks = this.user.tasks;
    }
  }

  public toggleNav(): void {
    console.log("Calling toggleNav!");
    this.drawer?.toggle();
  }

}
