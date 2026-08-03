from knowparex.PROGRAMMING_NOTES import compare_system
class starter:
    
    def iostream():
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "print(\"hello\")", "Python")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "fmt.Println(\"hello\")", "Go")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "console.log(\"hello\")", "JavaScript")
        compare_system.codesamebutsyntaxsimilar("#include <iostream> + std::cout << \"hello\" << std::endl;", "c++", "console.log(\"hello\")", "TypeScript")
    #| 標頭檔          | 功能                 |
    #| ------------ | ------------------ |
    #| `<iostream>` | `cout`、`cin`       |
    #| `<string>`   | `string`           |
    #| `<vector>`   | `vector`           |
    #| `<cmath>`    | 數學函式（`sqrt`、`pow`） |
    #| `<fstream>`  | 讀寫檔案               |
    #| `<cstdlib>`  | `rand()` 等工具       |
    #| `<ctime>`    | 時間相關函式             |
