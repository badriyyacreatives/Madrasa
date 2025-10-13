-- Madrasa Manager Supabase Database Schema

-- 1. Classes Table
CREATE TABLE classes (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Students Table
CREATE TABLE students (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    roll_number TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(class_id, roll_number)
);

-- 3. Attendance Table
CREATE TABLE attendance (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('present', 'late', 'absent')),
    time TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(class_id, student_id, date)
);

-- 4. Tasks Table
CREATE TABLE tasks (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('permanent', 'daily')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 5. Task Completion Table
CREATE TABLE task_completion (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
    student_id UUID REFERENCES students(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(task_id, student_id, date)
);

-- 6. Settings Table
CREATE TABLE settings (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    class_id UUID REFERENCES classes(id) ON DELETE CASCADE UNIQUE,
    grace_period INTEGER DEFAULT 5,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security (RLS) - Optional for public access
ALTER TABLE classes ENABLE ROW LEVEL SECURITY;
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
ALTER TABLE attendance ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_completion ENABLE ROW LEVEL SECURITY;
ALTER TABLE settings ENABLE ROW LEVEL SECURITY;

-- Create policies to allow public access (adjust as needed for your security requirements)
CREATE POLICY "Allow public read access on classes" ON classes FOR SELECT USING (true);
CREATE POLICY "Allow public insert on classes" ON classes FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on classes" ON classes FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on classes" ON classes FOR DELETE USING (true);

CREATE POLICY "Allow public read access on students" ON students FOR SELECT USING (true);
CREATE POLICY "Allow public insert on students" ON students FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on students" ON students FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on students" ON students FOR DELETE USING (true);

CREATE POLICY "Allow public read access on attendance" ON attendance FOR SELECT USING (true);
CREATE POLICY "Allow public insert on attendance" ON attendance FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on attendance" ON attendance FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on attendance" ON attendance FOR DELETE USING (true);

CREATE POLICY "Allow public read access on tasks" ON tasks FOR SELECT USING (true);
CREATE POLICY "Allow public insert on tasks" ON tasks FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on tasks" ON tasks FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on tasks" ON tasks FOR DELETE USING (true);

CREATE POLICY "Allow public read access on task_completion" ON task_completion FOR SELECT USING (true);
CREATE POLICY "Allow public insert on task_completion" ON task_completion FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on task_completion" ON task_completion FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on task_completion" ON task_completion FOR DELETE USING (true);

CREATE POLICY "Allow public read access on settings" ON settings FOR SELECT USING (true);
CREATE POLICY "Allow public insert on settings" ON settings FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public update on settings" ON settings FOR UPDATE USING (true);
CREATE POLICY "Allow public delete on settings" ON settings FOR DELETE USING (true);

-- Create indexes for better performance
CREATE INDEX idx_students_class_id ON students(class_id);
CREATE INDEX idx_attendance_class_date ON attendance(class_id, date);
CREATE INDEX idx_attendance_student_date ON attendance(student_id, date);
CREATE INDEX idx_tasks_class_id ON tasks(class_id);
CREATE INDEX idx_task_completion_date ON task_completion(task_id, date);
CREATE INDEX idx_settings_class_id ON settings(class_id);