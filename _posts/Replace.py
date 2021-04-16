import os, sys

count = 0
for folder in os.listdir():
    if not os.path.isfile(folder):
        print("Scan folder: "+folder)
        for subfolder in os.listdir(folder):
            if not os.path.isfile(folder+"/"+subfolder):
                print("\tScan subfolder: "+subfolder)
                for file in os.listdir(folder+"/"+subfolder):
                    pass
                    ## Step 1:
                    # if file.endswith(".md"):
                    #     with open(folder+"/"+subfolder+"/"+file, "r", encoding="utf-8") as f:
                    #         lines = f.readlines()
                    #     newlines = []
                    #     rename_flag = False
                    #     for line in lines:
                    #         if "github.io" in line:
                    #             rename_flag = True
                    #             break
                    #     if rename_flag == True:
                    #         count+=1
                    #         for line in lines:
                    #             if "github.io" in line:
                    #                 newlines.append(line.replace("github.io", "个站"))
                    #             else:
                    #                 newlines.append(line)
                    #         with open(folder+"/"+subfolder+"/"+file.replace(".md", "-副本.md"), "w", encoding="utf-8") as f:
                    #             for newline in newlines:
                    #                 f.write(newline)
                    #             print("\t\t"+file+"\t\tis done.")
                    
                    ## Step 2:
                    # if file.endswith("-副本.md"):
                    #     count+=1
                    #     os.remove(folder+"/"+subfolder+"/"+file.replace("-副本.md", ".md"))
                    #     os.rename(folder+"/"+subfolder+"/"+file, folder+"/"+subfolder+"/"+file.replace("-副本.md", ".md"))
                    #     print("\t\t"+file+"\t\tis done.")
            else:
                file = subfolder
                pass
                ## Step 1:
                # if file.endswith(".md"):
                #     with open(folder+"/"+file, "r", encoding="utf-8") as f:
                #         lines = f.readlines()
                #     newlines = []
                #     rename_flag = False
                #     for line in lines:
                #         if "github.io" in line:
                #             rename_flag = True
                #             break
                #     if rename_flag == True:
                #         count+=1
                #         for line in lines:
                #             if "github.io" in line:
                #                 newlines.append(line.replace("github.io", "个站"))
                #             else:
                #                 newlines.append(line)
                #         with open(folder+"/"+file.replace(".md", "-副本.md"), "w", encoding="utf-8") as f:
                #             for newline in newlines:
                #                 f.write(newline)
                #             print("\t"+file+"\t\tis done.")
                
                ## Step 2:
                # if file.endswith("-副本.md"):
                #     count+=1
                #     os.remove(folder+"/"+file.replace("-副本.md", ".md"))
                #     os.rename(folder+"/"+file, folder+"/"+file.replace("-副本.md", ".md"))
                #     print("\t"+file+"\t\tis done.")
print(count) # 149
