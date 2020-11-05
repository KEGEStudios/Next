#pragma once

#include <iostream>
#include <string>

#include <command_base.hpp>
#include <next_data.hpp>
#include <tools/exec.hpp>

class BuildCommand : public CommandBase
{
private:
    std::string name_project;
public:
    BuildCommand(/* args */);
    ~BuildCommand();
    int execute();
};