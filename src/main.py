import flet as ft

class Button(ft.ElevatedButton):
    def __init__(self,result,text,color=ft.Colors.WHITE,bg_color=ft.Colors.WHITE24,expand=1,func_text="0"):
        super().__init__(on_click=self.result_change,text=text,color=color,bgcolor=bg_color,style=ft.ButtonStyle(padding=10),expand=expand)
        self.result=result
        self.func_text=func_text
    def result_change(self,e):
        match self.func_text:
            case "":
                self.result.value="0"
                self.result.update()
                return
            case "+/-":
                try:
                    self.result.value=str(-1*int(self.result.value))
                    self.result.update()
                except:
                    pass
                return
            case "=":
                self.result.value=str(eval(self.result.value))
                self.result.update()
                return
        if self.result.value == "0":
            self.result.value=""
        self.result.value+=self.func_text
        self.result.update()
        
class App(ft.Container):
    def __init__(self):
        super().__init__(bgcolor=ft.Colors.BLACK,width=400,height=280,padding=15,border_radius=20)
        self.doing_widget()
    def doing_widget(self):
        #### Declaration ########
        self.result = ft.Text("0",color=ft.Colors.WHITE,size=20)
        #########################

        #### Add ################
        self.content = ft.Column([
            ft.Row([self.result],alignment=ft.MainAxisAlignment.END),
            ft.Row([Button(text="AC",color=ft.Colors.BLACK,bg_color=ft.Colors.BLUE_GREY_100,result=self.result,func_text=""),Button(text="+/-",color=ft.Colors.BLACK,bg_color=ft.Colors.BLUE_GREY_100,result=self.result,func_text="+/-"),Button(text="%",color=ft.Colors.BLACK,bg_color=ft.Colors.BLUE_GREY_100,result=self.result,func_text=" % "),Button(text="/",bg_color=ft.Colors.ORANGE,result=self.result,func_text="/")]),
            ft.Row([Button(text="7",result=self.result,func_text="7"),Button(text="8",result=self.result,func_text="8"),Button(text="9",result=self.result,func_text="9"),Button(text="*",bg_color=ft.Colors.ORANGE,result=self.result,func_text=" * ")]),
            ft.Row([Button(text="4",result=self.result,func_text="4"),Button(text="5",result=self.result,func_text="5"),Button(text="6",result=self.result,func_text="6"),Button(text="-",bg_color=ft.Colors.ORANGE,result=self.result,func_text=" - ")]),
            ft.Row([Button(text="1",result=self.result,func_text="1"),Button(text="2",result=self.result,func_text="2"),Button(text="3",result=self.result,func_text="3"),Button(text="+",bg_color=ft.Colors.ORANGE,result=self.result,func_text=" + ")]),
            ft.Row([Button(text="0",expand=3,result=self.result,func_text="0"),Button(text=".",result=self.result,func_text="."),Button(text="=",bg_color=ft.Colors.ORANGE,result=self.result,func_text="=")]),
        ])
        #########################

if __name__ == "__main__":
    def main(page : ft.Page):
        page.title="Calc App"
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        page.add(App())
    ft.app(main)