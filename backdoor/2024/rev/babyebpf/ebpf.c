#include<stdio.h>
#include<bpf/libbpf.h>
#include<unistd.h>

int main(){
    const char* filepath = "babyebpf.o";
    struct bpf_object* bpfObject;
    int err;

    bpfObject = bpf_object__open_file(filepath,NULL);
    if(!bpfObject){
        puts("Failed");
        return 1;
    }
    err = bpf_object__load(bpfObject);
    if(err){
        puts("Failed to load");
        return 1;
    }
    struct bpf_program *prog = bpf_object__find_program_by_name(bpfObject,"detect_execve");
    if(!prog){
        puts("Failed to find program");
        return 1;
    }
    bpf_program__attach(prog);
    while(1){

    }
    return 0;
}
