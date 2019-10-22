% target folder
if exist(bwcHostMatlab)
    fprintf('bwcHostMatlab =%s\n', bwcHostMatlab);
end

request_dir      = [bwcHostMatlab, '/request'];
request_dir_done = [bwcHostMatlab, '/request_done'];
fprintf('request_dir      =%s\n', request_dir);
fprintf('request_dir_done =%s\n', request_dir_done);

loop = 0; %loop time
WIDTH = 100;

while true
    loop = loop + 1;

    if (mod(loop, WIDTH) < (WIDTH/2))
        fprintf('.'); % just print .
    else
        fprintf('\b\b '); % just print .
    end
    %usleep(50000);
    pause(0.5);
    %sleep(1);

    %get the file lists in the request folder
    req = dir(request_dir);

    if (length(req) <= 2)
        continue;
    end

    %process the command in the request files
    for i=1:length(req)
        if req(i).isdir %ignore . and ..
            %fprintf('Ignore %s\n', req(i).name);
        else
            request_name      = [request_dir,      '/', req(i).name];
            request_name_done = [request_dir_done, '/', req(i).name];
            fprintf('request_name     =%s\n', request_name);
            fprintf('request_name_done=%s\n', request_name_done);

            %read the file content, then move the file to done foler
            fid = fopen(request_name, 'r');

            if fid == -1
                fprintf('File open error\n');
            else
                %fid = fopen('2017-02-06_Monday_14:41:25.447403_CST', 'r');
                %while (! feof(fid) )
                %    fprintf('%s\n', fgetl(fid));
                %end
                cmd.timeStamp     = fgetl(fid); %line 1
                cmd.datetimeStamp = fgetl(fid); %line 2
                cmd.addr          = fgetl(fid); %line 3
                cmd.data          = fgetl(fid); %line 4
                fprintf('cmd.data=%s\n', cmd.data);

                %extrace the user command
                %cmd.user_request = strtok(cmd.data); % find the first string befor seprator
                from_position = strfind(cmd.data, ' from');
                cmd.user_request = cmd.data(1 : (from_position - 1)); % find 'from'
                fprintf('cmd.user_request=%s\n', cmd.user_request);

                %execute the command
                try
                    eval(cmd.user_request);
                catch
                    fprintf(lasterr);
                    fprintf('\n');
                end

                fclose(fid);

                %move the file to new request_done folder
                system(sprintf('mv %s %s', request_name, request_name_done));
            end % if fid

        end % if req

    end %for
end % while
