// 파일 입출력
// 회원가입을 통해 아이디와 패스워드를 입력하여 userFile.txt 파일에 저장하고
// 로그인을 통해 아이디와 패스워드를 비교하여 결과를 출력하는 프로그램을 작성하시오.
#include<stdio.h>
#include<string.h>

int main(){
    
    FILE *fp;           // 파일 포인터
    char id[10];        // 사용자 입력 아이디
    char pw[12];        // 사용자 입력 비밀번호
    char savedId[10];   // 파일에 저장된 아이디
    char savedPw[12];   // 파일에 저장된 비밀번호
    int answer;
    
    printf("회원가입(1)/로그인(2) : ");
    scanf("%d", &answer);
    
    // 회원가입
    if(answer == 1){
        fp = fopen("userFile.txt", "a");        // 파일을 append 모드로 열기 (뒤에 추가)
        if (fp == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;   // 파열 열기 실패시 종료
        }
        // id 입력 받고 파일에 저장
        printf("아이디를 입력하세요 > ");
        scanf("%s", id);
        fprintf(fp,"%s\n", id);

        // pw 입력 받고 파일에 저장
        printf("비밀번호를 입력하세요 > ");
        scanf("%s", pw);
        fprintf(fp,"%s\n", pw);
        
        fclose(fp); // 파일 닫기
        printf("회원가입이 완료되었습니다.\n");

    }
    // 로그인
    else if(answer == 2){
        fp = fopen("userFile.txt", "r");        // 읽기 모드로 열기

        if (fp == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;   // 파열 열기 실패시 종료
        }

        // 로그인 정보 입력 받기
        printf("아이디를 입력하세요 > ");
        scanf("%s", id);

        printf("비밀번호를 입력하세요 > ");
        scanf("%s", pw);

        int loginSuccess = 0;   // 로그인 성공 여부 저장

        // 파일에서 아이디/비밀번호를 한 쌍씩 읽어서 비교
        while(fscanf(fp, "%s\n%s\n", savedId, savedPw) != EOF){
            if(strcmp(id, savedId) == 0 && strcmp(pw, savedPw) == 0){
                loginSuccess = 1;   // 일치하면 로그인 성공
                break;
            }
        }
        
        fclose(fp);     // 파일 닫기

        if(loginSuccess)
            printf("로그인 성공\n");
        else
            printf("아이디/비번 일치하지 않습니다.\n");
    }
    else{
        printf("다시 입력해주세요\n");
    }
    return 0;
}

