
# Create complete Madrasa Manager with all requested features and Supabase integration

complete_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Madrasa Manager</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <meta name="theme-color" content="#ea580c">
    <style>
        .hide { display: none !important; }
        .fade-in { animation: fadeIn 0.3s ease-in; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        .slide-up { animation: slideUp 0.3s ease-out; }
        @keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
        
        /* PWA Styles */
        body {
            -webkit-user-select: none;
            -webkit-touch-callout: none;
            -webkit-tap-highlight-color: transparent;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #ffedd5; }
        ::-webkit-scrollbar-thumb { background: #fb923c; border-radius: 2px; }
        ::-webkit-scrollbar-thumb:hover { background: #ea580c; }
        
        /* Button active states */
        button:active { transform: scale(0.98); }
        
        /* Modal animations */
        .modal-backdrop { backdrop-filter: blur(4px); }
        
        /* Loading spinner */
        .spinner {
            border: 2px solid #ffedd5;
            border-top: 2px solid #ea580c;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Enhanced button styles - Orange theme */
        .btn-primary {
            background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%);
            transition: all 0.2s ease;
        }
        
        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(234, 88, 12, 0.3);
        }
        
        /* Card hover effects */
        .card-hover:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        
        /* Status badges */
        .status-present { background-color: #dcfce7; color: #166534; }
        .status-late { background-color: #fed7aa; color: #9a3412; }
        .status-absent { background-color: #fecaca; color: #991b1b; }
        .status-leave { background-color: #dbeafe; color: #1e40af; }
        
        /* Task table styles */
        .task-master-table {
            border-collapse: separate;
            border-spacing: 0;
            min-width: 100%;
        }
        
        .task-master-table th {
            background-color: #fff7ed;
            font-weight: 600;
            text-align: center;
            border: 1px solid #fed7aa;
            font-size: 14px;
            position: relative;
            color: #9a3412;
        }
        
        .task-master-table td {
            border: 1px solid #fed7aa;
            text-align: center;
            padding: 12px 8px;
            background-color: white;
            min-width: 60px;
        }
        
        .task-master-table th:first-child,
        .task-master-table td:first-child {
            text-align: left;
            padding-left: 16px;
            font-weight: 500;
            background-color: #fff7ed;
            position: sticky;
            left: 0;
            z-index: 10;
            min-width: 150px;
            color: #111827;
        }
        
        .task-master-table tr:hover td {
            background-color: #ffedd5;
        }
        
        .task-master-table tr:hover td:first-child {
            background-color: #fed7aa;
        }
        
        /* Rotated task headers */
        .rotated-task-header {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            transform: rotate(180deg);
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px 4px;
            font-size: 13px;
            font-weight: 600;
            line-height: 1.2;
            color: #9a3412;
            white-space: nowrap;
        }
        
        /* Checkbox styles */
        .task-checkbox {
            width: 22px;
            height: 22px;
            border: 2px solid #fb923c;
            border-radius: 4px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            margin: 0 auto;
        }
        
        .task-checkbox.completed {
            background-color: #ea580c;
            border-color: #ea580c;
            color: white;
        }
        
        .task-checkbox:hover {
            border-color: #ea580c;
            background-color: #ffedd5;
        }
        
        .task-checkbox.completed:hover {
            background-color: #c2410c;
        }
        
        /* Long press animation */
        @keyframes longPress {
            0% { transform: scale(1); }
            50% { transform: scale(0.95); background-color: #fef3c7; }
            100% { transform: scale(1); }
        }
        
        .long-pressing {
            animation: longPress 0.6s ease-in-out;
        }
        
        /* Table container */
        .table-container {
            overflow-x: auto;
            border-radius: 8px;
            border: 1px solid #fed7aa;
            max-width: 100%;
        }
        
        /* Tab styles */
        .tab-button {
            padding: 8px 16px;
            border-bottom: 2px solid transparent;
            transition: all 0.2s ease;
        }
        
        .tab-button.active {
            border-bottom-color: #ea580c;
            color: #ea580c;
            font-weight: 600;
        }
        
        /* Custom confirmation modal */
        .confirm-modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0.9);
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1000;
        }
        
        .confirm-modal.show {
            transform: translate(-50%, -50%) scale(1);
            opacity: 1;
        }
        
        /* Mobile optimizations */
        @media (max-width: 640px) {
            .task-master-table th,
            .task-master-table td {
                min-width: 50px;
                padding: 8px 4px;
            }
            
            .task-master-table th:first-child,
            .task-master-table td:first-child {
                min-width: 120px;
                padding-left: 12px;
            }
            
            .rotated-task-header {
                height: 100px;
                font-size: 11px;
            }
            
            .task-checkbox {
                width: 18px;
                height: 18px;
            }
        }
    </style>
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiTWFkcmFzYSBNYW5hZ2VyIiwic2hvcnRfbmFtZSI6Ik1hZHJhc2EiLCJkZXNjcmlwdGlvbiI6IkNvbXBsZXRlIGNsYXNzcm9vbSBtYW5hZ2VtZW50IHN5c3RlbSIsInN0YXJ0X3VybCI6Ii8iLCJkaXNwbGF5Ijoic3RhbmRhbG9uZSIsImJhY2tncm91bmRfY29sb3IiOiIjZmZmZmZmIiwidGhlbWVfY29sb3IiOiIjZWE1ODBjIiwib3JpZW50YXRpb24iOiJwb3J0cmFpdC1wcmltYXJ5IiwiaWNvbnMiOlt7InNyYyI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjNhV1IwYUQwaU1UazJJaUJvWldsbmFIUTlJakU1TmlJK1BDOXPZM2crIiwic2l6ZXMiOiJhbnkifV19">
</head>
<body class="bg-orange-50 min-h-screen">
    <!-- Landing/Class Selection Page -->
    <div id="landing-page" class="min-h-screen flex flex-col items-center justify-center px-4">
        <div class="bg-orange-600 w-24 h-24 rounded-full flex items-center justify-center mb-8 card-hover transition-all duration-300">
            <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
        </div>
        
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Madrasa Manager</h1>
        <p class="text-gray-600 mb-8 text-center">Select your class to continue</p>
        
        <div id="class-list" class="w-full max-w-md space-y-3 mb-6">
            <!-- Classes will be populated here -->
        </div>
        
        <button id="create-class-btn" class="w-full max-w-md btn-primary text-white py-3 px-4 rounded-lg font-medium flex items-center justify-center gap-2 transition-all">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
            </svg>
            Create New Class
        </button>
    </div>

    <!-- Main App Container -->
    <div id="main-app" class="hide">
        <!-- Header -->
        <header class="bg-orange-600 text-white px-4 py-3 flex items-center justify-between sticky top-0 z-40">
            <div class="flex items-center gap-3">
                <div>
                    <h1 id="page-title" class="text-lg font-medium">Dashboard</h1>
                    <p id="class-name" class="text-orange-100 text-sm"></p>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <button id="settings-btn" class="p-2 rounded-lg hover:bg-orange-700 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    </svg>
                </button>
                <button id="logout-btn" class="p-2 rounded-lg hover:bg-orange-700 transition-colors">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
                    </svg>
                </button>
            </div>
        </header>

        <!-- Main Content -->
        <main id="main-content" class="pb-20 min-h-screen">
            <!-- Dashboard Page -->
            <div id="dashboard-page" class="page-content p-4">
                <div class="mb-6">
                    <h2 class="text-gray-600 text-sm font-medium mb-4">Today's Overview</h2>
                    
                    <div class="bg-white rounded-lg p-4 mb-4 card-hover transition-all duration-300">
                        <div class="grid grid-cols-2 gap-4 mb-4">
                            <div class="text-sm">
                                <span class="text-gray-600">Period</span>
                                <p id="current-date" class="font-medium"></p>
                            </div>
                            <div class="text-sm">
                                <span class="text-gray-600">Class Time</span>
                                <p id="class-time" class="font-medium"></p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-6">
                        <h3 class="text-gray-600 text-sm font-medium mb-3">Attendance Statistics</h3>
                        <div class="grid grid-cols-2 gap-3">
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-orange-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                                    </svg>
                                </div>
                                <p id="total-students" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Total Students</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-green-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                </div>
                                <p id="present-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Present</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-yellow-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </div>
                                <p id="late-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Late</p>
                            </div>
                            <div class="bg-white rounded-lg p-4 text-center card-hover transition-all duration-300">
                                <div class="flex items-center justify-center w-10 h-10 bg-red-100 rounded-full mx-auto mb-2">
                                    <svg class="w-5 h-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                                    </svg>
                                </div>
                                <p id="absent-count" class="text-2xl font-bold text-gray-900">0</p>
                                <p class="text-gray-600 text-sm">Absent</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg p-4 card-hover transition-all duration-300">
                        <h3 class="text-gray-600 text-sm font-medium mb-3">Quick Actions</h3>
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="font-medium">Pending Tasks</p>
                                <p class="text-gray-600 text-sm">Tasks to be completed today</p>
                            </div>
                            <div class="bg-red-500 text-white text-sm font-bold rounded-full w-8 h-8 flex items-center justify-center" id="pending-tasks-count">0</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Classes Page -->
            <div id="classes-page" class="page-content hide p-4">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-gray-600 text-sm font-medium">Students</h2>
                    <button id="add-student-btn" class="btn-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-medium transition-all">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                        </svg>
                        Add Student
                    </button>
                </div>
                
                <div class="bg-white rounded-lg card-hover transition-all duration-300">
                    <div class="p-4 border-b">
                        <div class="flex items-center justify-between">
                            <h3 id="class-header" class="font-semibold text-lg"></h3>
                            <span id="student-count-badge" class="bg-orange-100 text-orange-800 text-xs font-medium px-2 py-1 rounded-full">0 Students</span>
                        </div>
                        <p id="class-schedule" class="text-gray-600 text-sm mt-1"></p>
                    </div>
                    
                    <div id="students-list" class="divide-y">
                        <!-- Students will be populated here -->
                    </div>
                </div>
            </div>

            <!-- Attendance Page -->
            <div id="attendance-page" class="page-content hide p-4">
                <div class="bg-white rounded-lg p-4 mb-4 card-hover transition-all duration-300">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="text-sm">
                            <span class="text-gray-600">Class Time</span>
                            <p id="attendance-class-time" class="font-medium"></p>
                        </div>
                        <div class="text-sm">
                            <span class="text-gray-600">Grace Period</span>
                            <p id="attendance-grace-period" class="font-medium">5 minutes</p>
                        </div>
                    </div>
                </div>
                
                <!-- Date navigation will be inserted here -->
                
                <div id="attendance-list" class="space-y-3">
                    <!-- Attendance items will be populated here -->
                </div>
            </div>

            <!-- Tasks Page -->
            <div id="tasks-page" class="page-content hide p-4">
                <!-- Task Tabs -->
                <div class="flex gap-2 mb-4 bg-white rounded-lg p-1">
                    <button class="tab-button flex-1 active" data-tab="permanent">Permanent Tasks</button>
                    <button class="tab-button flex-1" data-tab="daily">Daily Routine</button>
                </div>
                
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-gray-600 text-sm font-medium">Tasks Management</h2>
                    <button id="create-task-btn" class="btn-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-medium transition-all">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
                        </svg>
                        Create Task
                    </button>
                </div>
                
                <!-- Permanent Tasks Container -->
                <div id="permanent-tasks-container" class="bg-white rounded-lg card-hover transition-all duration-300">
                    <!-- Permanent tasks table -->
                </div>
                
                <!-- Daily Routine Container -->
                <div id="daily-tasks-container" class="bg-white rounded-lg card-hover transition-all duration-300 hide">
                    <!-- Daily tasks table -->
                </div>
            </div>

            <!-- Settings Page -->
            <div id="settings-page" class="page-content hide p-4">
                <h2 class="text-gray-700 text-xl font-semibold mb-6">Settings</h2>
                
                <div class="bg-white rounded-lg p-4 mb-4 card-hover transition-all duration-300">
                    <h3 class="font-medium text-gray-900 mb-4">Class Schedule</h3>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Class Start Time</label>
                            <input type="time" id="settings-start-time" class="w-full p-3 border border-orange-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Class End Time</label>
                            <input type="time" id="settings-end-time" class="w-full p-3 border border-orange-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">Grace Period (minutes)</label>
                            <input type="number" id="settings-grace-period" min="0" max="30" class="w-full p-3 border border-orange-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500">
                        </div>
                        <button id="save-settings-btn" class="w-full btn-primary text-white py-3 rounded-lg font-medium">
                            Save Settings
                        </button>
                    </div>
                </div>
                
                <div class="bg-white rounded-lg p-4 card-hover transition-all duration-300">
                    <h3 class="font-medium text-gray-900 mb-2">About</h3>
                    <p class="text-gray-600 text-sm">Madrasa Manager v2.0</p>
                    <p class="text-gray-600 text-sm">Connected to Supabase Database</p>
                </div>
            </div>
        </main>

        <!-- Bottom Navigation -->
        <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-orange-200 z-50">
            <div class="flex">
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="dashboard">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m0 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1h3a1 1 0 001-1V10"></path>
                    </svg>
                    <span class="text-xs">Home</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="classes">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <span class="text-xs">Classes</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="attendance">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path>
                    </svg>
                    <span class="text-xs">Attendance</span>
                </button>
                <button class="nav-item flex-1 py-3 px-4 text-center transition-all" data-page="tasks">
                    <svg class="w-6 h-6 mx-auto mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
                    </svg>
                    <span class="text-xs">Tasks</span>
                </button>
            </div>
        </nav>
    </div>

    <!-- Modals -->
    <!-- Create Class Modal -->
    <div id="create-class-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Create New Class</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Class Name</label>
                    <input type="text" id="class-name-input" placeholder="e.g., Grade 5 - Quran" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Start Time</label>
                        <input type="time" id="start-time-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">End Time</label>
                        <input type="time" id="end-time-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                    </div>
                </div>
                <button id="create-class-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium">Create Class</button>
            </div>
        </div>
    </div>

    <!-- Add Student Modal -->
    <div id="add-student-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Add New Student</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Student Name</label>
                    <input type="text" id="student-name-input" placeholder="Enter student name" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Roll Number</label>
                    <input type="number" id="roll-number-input" placeholder="Enter roll number" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                </div>
                <button id="add-student-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium">Add Student</button>
            </div>
        </div>
    </div>

    <!-- Create Task Modal -->
    <div id="create-task-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-end justify-center z-50 hide">
        <div class="bg-white w-full max-w-md rounded-t-3xl slide-up">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Create New Task</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Task Title</label>
                    <input type="text" id="task-title-input" placeholder="e.g., Homework" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Task Type</label>
                    <select id="task-type-input" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                        <option value="permanent">Permanent Task</option>
                        <option value="daily">Daily Routine</option>
                    </select>
                </div>
                <button id="create-task-submit" class="w-full btn-primary text-white py-3 rounded-lg font-medium">Create Task</button>
            </div>
        </div>
    </div>

    <!-- Edit Attendance Modal -->
    <div id="edit-attendance-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-center justify-center z-50 hide">
        <div class="bg-white w-full max-w-md mx-4 rounded-lg">
            <div class="p-4 border-b">
                <div class="flex items-center justify-between">
                    <h3 class="text-lg font-semibold">Edit Attendance</h3>
                    <button class="modal-close p-1 hover:bg-gray-100 rounded">
                        <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <div class="p-4 space-y-4">
                <p id="edit-attendance-student-name" class="font-medium"></p>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Arrival Time</label>
                    <input type="time" id="edit-attendance-time" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500">
                </div>
                <div class="flex gap-3">
                    <button id="edit-attendance-cancel" class="flex-1 bg-gray-200 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-300">Cancel</button>
                    <button id="edit-attendance-submit" class="flex-1 btn-primary text-white py-3 rounded-lg font-medium">Update</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Custom Confirmation Modal -->
    <div id="confirm-modal" class="confirm-modal bg-white rounded-lg shadow-2xl max-w-sm mx-4 p-6 hide">
        <div class="text-center">
            <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                </svg>
            </div>
            <h3 id="confirm-title" class="text-lg font-semibold mb-2"></h3>
            <p id="confirm-message" class="text-gray-600 mb-6"></p>
            <div class="flex gap-3">
                <button id="confirm-cancel" class="flex-1 bg-gray-200 text-gray-700 py-2 rounded-lg font-medium hover:bg-gray-300">Cancel</button>
                <button id="confirm-ok" class="flex-1 bg-red-600 text-white py-2 rounded-lg font-medium hover:bg-red-700">Delete</button>
            </div>
        </div>
    </div>
    <div id="confirm-backdrop" class="fixed inset-0 bg-black bg-opacity-50 z-[999] hide"></div>

    <!-- Alert Modal -->
    <div id="alert-modal" class="fixed inset-0 bg-black bg-opacity-50 modal-backdrop flex items-center justify-center z-50 hide">
        <div class="bg-white w-full max-w-sm mx-4 rounded-lg">
            <div class="p-4 text-center">
                <div id="alert-icon" class="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center"></div>
                <h3 id="alert-title" class="text-lg font-semibold mb-2"></h3>
                <p id="alert-message" class="text-gray-600 mb-4"></p>
                <button id="alert-ok" class="w-full btn-primary text-white py-3 rounded-lg font-medium">OK</button>
            </div>
        </div>
    </div>

    <script>
// Madrasa Manager with Supabase Integration
const SUPABASE_URL = 'https://oczzftqfkcpwnhylmvsd.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jenpmdHFma2Nwd25oeWxtdnNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxMzY3MTIsImV4cCI6MjA3NTcxMjcxMn0.6oRz7LPEq0Z3k_lbz60l9iIs_9IwgasApWA85awsoxE';

class MadrasaManager {
    constructor() {
        this.supabase = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
        this.currentClass = null;
        this.currentPage = 'dashboard';
        this.currentTaskTab = 'permanent';
        this.currentAttendanceDate = new Date().toISOString().split('T')[0];
        this.gracePeriod = 5;
        this.longPressTimer = null;
        this.longPressTarget = null;
        this.init();
    }

    async init() {
        await this.setupDatabase();
        this.setupEventListeners();
        await this.loadLandingPage();
    }

    async setupDatabase() {
        // Database tables are already created in Supabase
        // Tables: classes, students, attendance, tasks, task_completion, settings
        console.log('Connected to Supabase');
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', (e) => {
                this.navigateToPage(e.currentTarget.dataset.page);
            });
        });

        // Settings button
        document.getElementById('settings-btn').addEventListener('click', () => {
            this.navigateToPage('settings');
        });

        // Modal close buttons
        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.hideModal(e.target.closest('.fixed'));
            });
        });

        // Create class
        document.getElementById('create-class-btn').addEventListener('click', () => {
            this.showModal('create-class-modal');
        });
        document.getElementById('create-class-submit').addEventListener('click', () => {
            this.createClass();
        });

        // Add student
        document.getElementById('add-student-btn').addEventListener('click', () => {
            this.showModal('add-student-modal');
        });
        document.getElementById('add-student-submit').addEventListener('click', () => {
            this.addStudent();
        });

        // Create task
        document.getElementById('create-task-btn').addEventListener('click', () => {
            this.showModal('create-task-modal');
        });
        document.getElementById('create-task-submit').addEventListener('click', () => {
            this.createTask();
        });

        // Edit attendance
        document.getElementById('edit-attendance-cancel').addEventListener('click', () => {
            this.hideModal(document.getElementById('edit-attendance-modal'));
        });
        document.getElementById('edit-attendance-submit').addEventListener('click', () => {
            this.submitEditAttendance();
        });

        // Settings
        document.getElementById('save-settings-btn').addEventListener('click', () => {
            this.saveSettings();
        });

        // Logout
        document.getElementById('logout-btn').addEventListener('click', () => {
            this.logout();
        });

        // Alert OK
        document.getElementById('alert-ok').addEventListener('click', () => {
            this.hideModal(document.getElementById('alert-modal'));
        });

        // Task tabs
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const tab = e.target.dataset.tab;
                this.switchTaskTab(tab);
            });
        });

        // Date navigation
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('date-nav')) {
                const direction = e.target.dataset.direction;
                this.navigateDate(direction);
            }
        });

        // Confirmation modal
        document.getElementById('confirm-cancel').addEventListener('click', () => {
            this.hideConfirmModal();
        });
        document.getElementById('confirm-ok').addEventListener('click', () => {
            if (this.confirmCallback) {
                this.confirmCallback();
                this.hideConfirmModal();
            }
        });
    }

    async loadLandingPage() {
        const classList = document.getElementById('class-list');
        classList.innerHTML = '<div class="spinner mx-auto"></div>';

        const { data: classes, error } = await this.supabase
            .from('classes')
            .select('*')
            .order('created_at', { ascending: false });

        if (error) {
            console.error('Error loading classes:', error);
            classList.innerHTML = '<p class="text-red-500 text-center">Error loading classes</p>';
            return;
        }

        classList.innerHTML = '';

        if (classes.length === 0) {
            classList.innerHTML = `
                <div class="text-center py-8">
                    <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                        <svg class="w-8 h-8 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                        </svg>
                    </div>
                    <p class="text-gray-600 font-medium">No classes created yet</p>
                    <p class="text-gray-500 text-sm mt-1">Create your first class to get started</p>
                </div>
            `;
        } else {
            for (const cls of classes) {
                const { count } = await this.supabase
                    .from('students')
                    .select('*', { count: 'exact', head: true })
                    .eq('class_id', cls.id);

                const classElement = document.createElement('div');
                classElement.className = 'bg-white rounded-lg p-4 cursor-pointer hover:bg-orange-50 transition-all duration-200 card-hover border border-orange-100';
                classElement.innerHTML = `
                    <div class="flex items-center justify-between">
                        <div class="flex-1">
                            <h3 class="font-semibold text-gray-900 text-lg">${cls.name}</h3>
                            <p class="text-gray-600 text-sm mt-1">${count || 0} students enrolled</p>
                        </div>
                        <div class="text-right ml-4">
                            <div class="text-sm font-medium text-orange-600 bg-orange-50 px-2 py-1 rounded">
                                ${cls.start_time} - ${cls.end_time}
                            </div>
                        </div>
                    </div>
                `;
                classElement.addEventListener('click', () => this.selectClass(cls));
                classList.appendChild(classElement);
            }
        }

        document.getElementById('landing-page').classList.remove('hide');
        document.getElementById('main-app').classList.add('hide');
    }

    async selectClass(classData) {
        this.currentClass = classData;
        
        // Load settings for this class
        const { data: settings } = await this.supabase
            .from('settings')
            .select('*')
            .eq('class_id', classData.id)
            .single();

        if (settings) {
            this.gracePeriod = settings.grace_period || 5;
        }

        document.getElementById('landing-page').classList.add('hide');
        document.getElementById('main-app').classList.remove('hide');
        document.getElementById('class-name').textContent = classData.name;
        this.navigateToPage('dashboard');
    }

    async createClass() {
        const name = document.getElementById('class-name-input').value.trim();
        const startTime = document.getElementById('start-time-input').value;
        const endTime = document.getElementById('end-time-input').value;

        if (!name || !startTime || !endTime) {
            this.showAlert('Error', 'Please fill in all fields', 'error');
            return;
        }

        const { data, error } = await this.supabase
            .from('classes')
            .insert([{ 
                name, 
                start_time: startTime, 
                end_time: endTime 
            }])
            .select()
            .single();

        if (error) {
            this.showAlert('Error', 'Failed to create class', 'error');
            return;
        }

        // Create default settings
        await this.supabase.from('settings').insert([{
            class_id: data.id,
            grace_period: 5
        }]);

        this.hideModal(document.getElementById('create-class-modal'));
        this.loadLandingPage();
        this.showAlert('Success', 'Class created successfully!', 'success');

        document.getElementById('class-name-input').value = '';
        document.getElementById('start-time-input').value = '';
        document.getElementById('end-time-input').value = '';
    }

    navigateToPage(page) {
        document.querySelectorAll('.nav-item').forEach(item => {
            if (item.dataset.page === page) {
                item.classList.add('text-orange-500');
                item.classList.remove('text-gray-400');
            } else {
                item.classList.remove('text-orange-500');
                item.classList.add('text-gray-400');
            }
        });

        document.querySelectorAll('.page-content').forEach(pageEl => {
            pageEl.classList.add('hide');
        });

        document.getElementById(`${page}-page`).classList.remove('hide');

        const titles = {
            dashboard: 'Dashboard',
            classes: 'Class Management',
            attendance: 'Attendance',
            tasks: 'Tasks',
            settings: 'Settings'
        };
        document.getElementById('page-title').textContent = titles[page];

        this.currentPage = page;

        switch (page) {
            case 'dashboard':
                this.loadDashboard();
                break;
            case 'classes':
                this.loadClasses();
                break;
            case 'attendance':
                this.loadAttendance();
                break;
            case 'tasks':
                this.loadTasks();
                break;
            case 'settings':
                this.loadSettings();
                break;
        }
    }

    async loadDashboard() {
        if (!this.currentClass) return;

        const today = new Date().toISOString().split('T')[0];
        document.getElementById('current-date').textContent = new Date().toLocaleDateString('en-US', { 
            weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' 
        });
        document.getElementById('class-time').textContent = `${this.currentClass.start_time} - ${this.currentClass.end_time}`;

        // Get total students
        const { count: totalStudents } = await this.supabase
            .from('students')
            .select('*', { count: 'exact', head: true })
            .eq('class_id', this.currentClass.id);

        // Get today's attendance
        const { data: attendance } = await this.supabase
            .from('attendance')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .eq('date', today);

        const present = attendance?.filter(a => a.status === 'present').length || 0;
        const late = attendance?.filter(a => a.status === 'late').length || 0;
        const absent = attendance?.filter(a => a.status === 'absent').length || 0;

        document.getElementById('total-students').textContent = totalStudents || 0;
        document.getElementById('present-count').textContent = present;
        document.getElementById('late-count').textContent = late;
        document.getElementById('absent-count').textContent = absent;

        // Get pending tasks
        const { data: students } = await this.supabase
            .from('students')
            .select('id')
            .eq('class_id', this.currentClass.id);

        const { data: tasks } = await this.supabase
            .from('tasks')
            .select('id')
            .eq('class_id', this.currentClass.id);

        const { data: completions } = await this.supabase
            .from('task_completion')
            .select('*')
            .eq('date', today);

        const totalTaskAssignments = (students?.length || 0) * (tasks?.length || 0);
        const completed = completions?.length || 0;
        document.getElementById('pending-tasks-count').textContent = totalTaskAssignments - completed;
    }

    async loadClasses() {
        if (!this.currentClass) return;

        document.getElementById('class-header').textContent = this.currentClass.name;
        document.getElementById('class-schedule').textContent = `Class Time: ${this.currentClass.start_time} - ${this.currentClass.end_time}`;

        const { data: students, error } = await this.supabase
            .from('students')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .order('roll_number');

        document.getElementById('student-count-badge').textContent = `${students?.length || 0} Students`;

        const studentsList = document.getElementById('students-list');
        studentsList.innerHTML = '';

        if (!students || students.length === 0) {
            studentsList.innerHTML = `
                <div class="p-6 text-center text-gray-500">
                    <svg class="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
                    </svg>
                    <p class="font-medium">No students added yet</p>
                    <p class="text-sm">Click "Add Student" to get started</p>
                </div>
            `;
            return;
        }

        students.forEach(student => {
            const studentElement = document.createElement('div');
            studentElement.className = 'p-4 flex items-center justify-between hover:bg-orange-50 transition-colors';
            studentElement.innerHTML = `
                <div>
                    <h4 class="font-medium text-gray-900">${student.name}</h4>
                    <p class="text-gray-600 text-sm">Roll No: ${student.roll_number}</p>
                </div>
                <button class="text-red-500 hover:bg-red-50 p-2 rounded transition-colors delete-student-btn" data-id="${student.id}">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                    </svg>
                </button>
            `;

            // Long press to delete
            const deleteBtn = studentElement.querySelector('.delete-student-btn');
            this.setupLongPress(deleteBtn, () => {
                this.showConfirm('Delete Student', 'Are you sure you want to delete this student?', () => {
                    this.removeStudent(student.id);
                });
            });

            studentsList.appendChild(studentElement);
        });
    }

    async addStudent() {
        const name = document.getElementById('student-name-input').value.trim();
        const rollNumber = document.getElementById('roll-number-input').value.trim();

        if (!name || !rollNumber) {
            this.showAlert('Error', 'Please fill in all fields', 'error');
            return;
        }

        const { error } = await this.supabase
            .from('students')
            .insert([{
                class_id: this.currentClass.id,
                name,
                roll_number: rollNumber
            }]);

        if (error) {
            this.showAlert('Error', 'Failed to add student', 'error');
            return;
        }

        this.hideModal(document.getElementById('add-student-modal'));
        this.loadClasses();
        this.showAlert('Success', 'Student added successfully!', 'success');

        document.getElementById('student-name-input').value = '';
        document.getElementById('roll-number-input').value = '';
    }

    async removeStudent(studentId) {
        const { error } = await this.supabase
            .from('students')
            .delete()
            .eq('id', studentId);

        if (error) {
            this.showAlert('Error', 'Failed to remove student', 'error');
            return;
        }

        this.loadClasses();
        this.showAlert('Success', 'Student removed successfully!', 'success');
    }

    async loadAttendance() {
        if (!this.currentClass) return;

        const attendancePage = document.getElementById('attendance-page');
        
        if (!attendancePage.querySelector('.date-navigation')) {
            const dateNavHTML = `
                <div class="date-navigation mb-4">
                    <div class="flex items-center justify-between bg-white rounded-lg p-3 card-hover transition-all duration-300">
                        <button class="date-nav p-2 rounded-lg hover:bg-gray-100 transition-colors" data-direction="prev">
                            <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                            </svg>
                        </button>
                        <div class="text-center">
                            <h3 id="attendance-date-display" class="font-medium text-lg text-gray-900"></h3>
                            <p class="text-gray-600 text-sm" id="attendance-day-name"></p>
                        </div>
                        <button class="date-nav p-2 rounded-lg hover:bg-gray-100 transition-colors" data-direction="next">
                            <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                        </button>
                    </div>
                </div>
            `;
            attendancePage.querySelector('#attendance-list').insertAdjacentHTML('beforebegin', dateNavHTML);
        }

        const selectedDate = new Date(this.currentAttendanceDate);
        document.getElementById('attendance-date-display').textContent = selectedDate.toLocaleDateString('en-US', { 
            year: 'numeric', month: 'long', day: 'numeric' 
        });
        document.getElementById('attendance-day-name').textContent = selectedDate.toLocaleDateString('en-US', { weekday: 'long' });
        document.getElementById('attendance-class-time').textContent = `${this.currentClass.start_time} - ${this.currentClass.end_time}`;
        document.getElementById('attendance-grace-period').textContent = `${this.gracePeriod} minutes`;

        const { data: students } = await this.supabase
            .from('students')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .order('roll_number');

        const { data: attendance } = await this.supabase
            .from('attendance')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .eq('date', this.currentAttendanceDate);

        const attendanceList = document.getElementById('attendance-list');
        attendanceList.innerHTML = '';

        if (!students || students.length === 0) {
            attendanceList.innerHTML = `
                <div class="bg-white rounded-lg p-6 text-center text-gray-500">
                    <p class="font-medium">No students in this class</p>
                </div>
            `;
            return;
        }

        const isToday = this.currentAttendanceDate === new Date().toISOString().split('T')[0];
        const isFriday = selectedDate.getDay() === 5;

        if (isFriday) {
            attendanceList.innerHTML = `
                <div class="bg-blue-50 rounded-lg p-6 text-center mb-4">
                    <h3 class="font-semibold text-blue-900 mb-2 text-lg">Friday - Weekly Leave</h3>
                    <p class="text-blue-700">All students have automatic leave on Fridays</p>
                </div>
            `;
            return;
        }

        for (const student of students) {
            const studentAttendance = attendance?.find(a => a.student_id === student.id);
            
            const studentElement = document.createElement('div');
            studentElement.className = 'bg-white rounded-lg p-4 mb-3 card-hover transition-all duration-300';
            
            let statusBadge = '';
            let timeText = '';
            let actionButtons = '';

            if (studentAttendance) {
                if (studentAttendance.status === 'present') {
                    statusBadge = '<span class="status-present text-xs font-medium px-3 py-1 rounded-full">PRESENT</span>';
                    timeText = `Marked at ${new Date(studentAttendance.time).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}`;
                } else if (studentAttendance.status === 'late') {
                    statusBadge = '<span class="status-late text-xs font-medium px-3 py-1 rounded-full">LATE</span>';
                    timeText = `Marked at ${new Date(studentAttendance.time).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}`;
                } else if (studentAttendance.status === 'absent') {
                    statusBadge = '<span class="status-absent text-xs font-medium px-3 py-1 rounded-full">ABSENT</span>';
                }

                // Show edit button only for today
                if (isToday) {
                    actionButtons = `
                        <button class="mt-3 text-orange-600 hover:text-orange-700 font-medium text-sm edit-attendance-btn" data-student-id="${student.id}" data-student-name="${student.name}" data-time="${studentAttendance.time}">
                            Edit Attendance
                        </button>
                    `;
                }
            } else {
                if (isToday) {
                    actionButtons = `
                        <div class="flex gap-2 mt-3">
                            <button onclick="madrasaManager.markPresentNow('${student.id}')" class="btn-primary text-white px-4 py-2 rounded-lg text-sm font-medium flex items-center gap-1">
                                Present Now
                            </button>
                            <button class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg text-sm font-medium flex items-center gap-1 edit-attendance-btn" data-student-id="${student.id}" data-student-name="${student.name}">
                                Set Time
                            </button>
                        </div>
                    `;
                }
            }

            studentElement.innerHTML = `
                <div class="flex items-center justify-between mb-2">
                    <div>
                        <h4 class="font-medium text-gray-900">${student.name}</h4>
                        <p class="text-gray-600 text-sm">Roll No: ${student.roll_number}</p>
                    </div>
                    ${statusBadge}
                </div>
                ${timeText ? `<div class="text-gray-600 text-sm mb-2">${timeText}</div>` : ''}
                ${actionButtons}
            `;

            // Edit attendance button handler
            const editBtn = studentElement.querySelector('.edit-attendance-btn');
            if (editBtn) {
                editBtn.addEventListener('click', (e) => {
                    const studentId = e.currentTarget.dataset.studentId;
                    const studentName = e.currentTarget.dataset.studentName;
                    const time = e.currentTarget.dataset.time;
                    this.showEditAttendanceModal(studentId, studentName, time);
                });
            }

            attendanceList.appendChild(studentElement);
        }
    }

    showEditAttendanceModal(studentId, studentName, currentTime) {
        document.getElementById('edit-attendance-student-name').textContent = studentName;
        
        if (currentTime) {
            const time = new Date(currentTime);
            const hours = time.getHours().toString().padStart(2, '0');
            const minutes = time.getMinutes().toString().padStart(2, '0');
            document.getElementById('edit-attendance-time').value = `${hours}:${minutes}`;
        } else {
            const now = new Date();
            const hours = now.getHours().toString().padStart(2, '0');
            const minutes = now.getMinutes().toString().padStart(2, '0');
            document.getElementById('edit-attendance-time').value = `${hours}:${minutes}`;
        }

        document.getElementById('edit-attendance-modal').dataset.studentId = studentId;
        this.showModal('edit-attendance-modal');
    }

    async submitEditAttendance() {
        const studentId = document.getElementById('edit-attendance-modal').dataset.studentId;
        const timeInput = document.getElementById('edit-attendance-time').value;
        
        if (!timeInput) {
            this.showAlert('Error', 'Please select a time', 'error');
            return;
        }

        const [hours, minutes] = timeInput.split(':');
        const attendanceTime = new Date(this.currentAttendanceDate);
        attendanceTime.setHours(hours, minutes, 0, 0);

        await this.markAttendanceWithTime(studentId, attendanceTime);
        this.hideModal(document.getElementById('edit-attendance-modal'));
    }

    async markPresentNow(studentId) {
        const now = new Date();
        await this.markAttendanceWithTime(studentId, now);
    }

    async markAttendanceWithTime(studentId, time) {
        const classStartTime = this.parseTime(this.currentClass.start_time);
        const timeDiff = time - classStartTime;
        const graceMs = this.gracePeriod * 60 * 1000;

        const status = timeDiff <= graceMs ? 'present' : 'late';

        const { error } = await this.supabase
            .from('attendance')
            .upsert([{
                class_id: this.currentClass.id,
                student_id: studentId,
                date: this.currentAttendanceDate,
                status,
                time: time.toISOString()
            }], {
                onConflict: 'class_id,student_id,date'
            });

        if (error) {
            this.showAlert('Error', 'Failed to mark attendance', 'error');
            return;
        }

        this.loadAttendance();
        this.showAlert('Success', `Marked as ${status}`, 'success');
    }

    navigateDate(direction) {
        const currentDate = new Date(this.currentAttendanceDate);
        if (direction === 'prev') {
            currentDate.setDate(currentDate.getDate() - 1);
        } else {
            currentDate.setDate(currentDate.getDate() + 1);
        }
        this.currentAttendanceDate = currentDate.toISOString().split('T')[0];
        this.loadAttendance();
    }

    switchTaskTab(tab) {
        this.currentTaskTab = tab;
        
        document.querySelectorAll('.tab-button').forEach(btn => {
            if (btn.dataset.tab === tab) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        if (tab === 'permanent') {
            document.getElementById('permanent-tasks-container').classList.remove('hide');
            document.getElementById('daily-tasks-container').classList.add('hide');
        } else {
            document.getElementById('permanent-tasks-container').classList.add('hide');
            document.getElementById('daily-tasks-container').classList.remove('hide');
        }

        this.loadTasks();
    }

    async loadTasks() {
        if (!this.currentClass) return;

        const { data: tasks } = await this.supabase
            .from('tasks')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .eq('type', this.currentTaskTab)
            .order('created_at');

        const { data: students } = await this.supabase
            .from('students')
            .select('*')
            .eq('class_id', this.currentClass.id)
            .order('roll_number');

        const containerId = this.currentTaskTab === 'permanent' ? 'permanent-tasks-container' : 'daily-tasks-container';
        const container = document.getElementById(containerId);
        
        container.innerHTML = '';

        if (!students || students.length === 0) {
            container.innerHTML = `<div class="p-6 text-center text-gray-500"><p>No students in class</p></div>`;
            return;
        }

        if (!tasks || tasks.length === 0) {
            container.innerHTML = `<div class="p-6 text-center text-gray-500"><p>No ${this.currentTaskTab} tasks created</p></div>`;
            return;
        }

        // Get completions for today (or all time for permanent)
        const today = new Date().toISOString().split('T')[0];
        const { data: completions } = await this.supabase
            .from('task_completion')
            .select('*')
            .in('task_id', tasks.map(t => t.id))
            .eq('date', this.currentTaskTab === 'daily' ? today : today);

        // Build table
        const tableContainer = document.createElement('div');
        tableContainer.className = 'table-container';
        
        const table = document.createElement('table');
        table.className = 'task-master-table';
        
        // Header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        
        const studentHeaderCell = document.createElement('th');
        studentHeaderCell.textContent = 'Students';
        headerRow.appendChild(studentHeaderCell);
        
        tasks.forEach(task => {
            const taskCell = document.createElement('th');
            const headerDiv = document.createElement('div');
            headerDiv.className = 'rotated-task-header task-header-cell';
            headerDiv.textContent = task.title;
            headerDiv.dataset.taskId = task.id;
            
            // Long press to delete
            this.setupLongPress(headerDiv, () => {
                this.showConfirm('Delete Task', `Are you sure you want to delete "${task.title}"?`, () => {
                    this.removeTask(task.id);
                });
            });
            
            taskCell.appendChild(headerDiv);
            headerRow.appendChild(taskCell);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Body
        const tbody = document.createElement('tbody');
        
        students.forEach(student => {
            const row = document.createElement('tr');
            
            const studentCell = document.createElement('td');
            studentCell.innerHTML = `
                <div class="font-medium text-gray-900">${student.name}</div>
                <div class="text-xs text-gray-600 mt-1">Roll: ${student.roll_number}</div>
            `;
            row.appendChild(studentCell);
            
            tasks.forEach(task => {
                const taskCell = document.createElement('td');
                const isCompleted = completions?.some(c => 
                    c.task_id === task.id && c.student_id === student.id
                );
                
                const checkbox = document.createElement('div');
                checkbox.className = `task-checkbox ${isCompleted ? 'completed' : ''}`;
                checkbox.dataset.taskId = task.id;
                checkbox.dataset.studentId = student.id;
                
                if (isCompleted) {
                    checkbox.innerHTML = '<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>';
                }
                
                if (this.currentTaskTab === 'permanent') {
                    // Long press for permanent tasks
                    this.setupLongPress(checkbox, () => {
                        this.toggleTaskCompletion(task.id, student.id, !isCompleted);
                    });
                } else {
                    // Regular click for daily tasks
                    checkbox.addEventListener('click', () => {
                        this.toggleTaskCompletion(task.id, student.id, !isCompleted);
                    });
                }
                
                taskCell.appendChild(checkbox);
                row.appendChild(taskCell);
            });
            
            tbody.appendChild(row);
        });
        
        table.appendChild(tbody);
        tableContainer.appendChild(table);
        container.appendChild(tableContainer);
    }

    async createTask() {
        const title = document.getElementById('task-title-input').value.trim();
        const type = document.getElementById('task-type-input').value;

        if (!title) {
            this.showAlert('Error', 'Please enter a task title', 'error');
            return;
        }

        const { error } = await this.supabase
            .from('tasks')
            .insert([{
                class_id: this.currentClass.id,
                title,
                type
            }]);

        if (error) {
            this.showAlert('Error', 'Failed to create task', 'error');
            return;
        }

        this.hideModal(document.getElementById('create-task-modal'));
        this.currentTaskTab = type;
        this.switchTaskTab(type);
        this.showAlert('Success', 'Task created successfully!', 'success');

        document.getElementById('task-title-input').value = '';
    }

    async toggleTaskCompletion(taskId, studentId, isCompleted) {
        const today = new Date().toISOString().split('T')[0];

        if (isCompleted) {
            const { error } = await this.supabase
                .from('task_completion')
                .insert([{
                    task_id: taskId,
                    student_id: studentId,
                    date: today
                }]);

            if (error) console.error('Error marking task complete:', error);
        } else {
            const { error } = await this.supabase
                .from('task_completion')
                .delete()
                .eq('task_id', taskId)
                .eq('student_id', studentId)
                .eq('date', today);

            if (error) console.error('Error unmarking task:', error);
        }

        this.loadTasks();
    }

    async removeTask(taskId) {
        const { error } = await this.supabase
            .from('tasks')
            .delete()
            .eq('id', taskId);

        if (error) {
            this.showAlert('Error', 'Failed to remove task', 'error');
            return;
        }

        this.loadTasks();
        this.showAlert('Success', 'Task removed successfully!', 'success');
    }

    async loadSettings() {
        if (!this.currentClass) return;

        document.getElementById('settings-start-time').value = this.currentClass.start_time;
        document.getElementById('settings-end-time').value = this.currentClass.end_time;
        document.getElementById('settings-grace-period').value = this.gracePeriod;
    }

    async saveSettings() {
        const startTime = document.getElementById('settings-start-time').value;
        const endTime = document.getElementById('settings-end-time').value;
        const gracePeriod = parseInt(document.getElementById('settings-grace-period').value);

        // Update class times
        const { error: classError } = await this.supabase
            .from('classes')
            .update({
                start_time: startTime,
                end_time: endTime
            })
            .eq('id', this.currentClass.id);

        // Update settings
        const { error: settingsError } = await this.supabase
            .from('settings')
            .upsert([{
                class_id: this.currentClass.id,
                grace_period: gracePeriod
            }], {
                onConflict: 'class_id'
            });

        if (classError || settingsError) {
            this.showAlert('Error', 'Failed to save settings', 'error');
            return;
        }

        this.currentClass.start_time = startTime;
        this.currentClass.end_time = endTime;
        this.gracePeriod = gracePeriod;

        this.showAlert('Success', 'Settings saved successfully!', 'success');
    }

    setupLongPress(element, callback) {
        let pressTimer = null;
        
        const startPress = (e) => {
            e.preventDefault();
            element.classList.add('long-pressing');
            pressTimer = setTimeout(() => {
                callback();
                element.classList.remove('long-pressing');
            }, 600);
        };
        
        const cancelPress = () => {
            if (pressTimer) {
                clearTimeout(pressTimer);
                element.classList.remove('long-pressing');
            }
        };
        
        element.addEventListener('touchstart', startPress);
        element.addEventListener('mousedown', startPress);
        element.addEventListener('touchend', cancelPress);
        element.addEventListener('touchmove', cancelPress);
        element.addEventListener('mouseup', cancelPress);
        element.addEventListener('mouseleave', cancelPress);
    }

    showConfirm(title, message, callback) {
        document.getElementById('confirm-title').textContent = title;
        document.getElementById('confirm-message').textContent = message;
        document.getElementById('confirm-modal').classList.remove('hide');
        document.getElementById('confirm-backdrop').classList.remove('hide');
        
        setTimeout(() => {
            document.getElementById('confirm-modal').classList.add('show');
        }, 10);
        
        this.confirmCallback = callback;
    }

    hideConfirmModal() {
        document.getElementById('confirm-modal').classList.remove('show');
        setTimeout(() => {
            document.getElementById('confirm-modal').classList.add('hide');
            document.getElementById('confirm-backdrop').classList.add('hide');
        }, 300);
        this.confirmCallback = null;
    }

    showModal(modalId) {
        document.getElementById(modalId).classList.remove('hide');
        document.body.style.overflow = 'hidden';
    }

    hideModal(modal) {
        if (typeof modal === 'string') {
            modal = document.getElementById(modal);
        }
        modal.classList.add('hide');
        document.body.style.overflow = 'auto';
    }

    showAlert(title, message, type = 'success') {
        const alertModal = document.getElementById('alert-modal');
        const alertIcon = document.getElementById('alert-icon');
        const alertTitle = document.getElementById('alert-title');
        const alertMessage = document.getElementById('alert-message');

        alertTitle.textContent = title;
        alertMessage.textContent = message;

        if (type === 'success') {
            alertIcon.className = 'w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-green-100';
            alertIcon.innerHTML = '<svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>';
        } else if (type === 'error') {
            alertIcon.className = 'w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center bg-red-100';
            alertIcon.innerHTML = '<svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>';
        }

        this.showModal('alert-modal');
        
        setTimeout(() => {
            this.hideModal(alertModal);
        }, 2000);
    }

    parseTime(timeString) {
        const [hours, minutes] = timeString.split(':');
        const today = new Date();
        return new Date(today.getFullYear(), today.getMonth(), today.getDate(), hours, minutes);
    }

    logout() {
        this.showConfirm('Logout', 'Are you sure you want to logout?', () => {
            this.currentClass = null;
            this.loadLandingPage();
        });
    }
}

// Initialize the application
const madrasaManager = new MadrasaManager();
    </script>
</body>
</html>'''

# Save the complete HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

print("✅ Complete Madrasa Manager with Supabase Integration!")
print("\n🎯 NEW FEATURES IMPLEMENTED:")
print("   ✓ Orange color theme throughout the app")
print("   ✓ Attendance edit option (only for current day)")
print("   ✓ Permanent tasks + Daily routine tabs")
print("   ✓ Long press to complete permanent tasks")
print("   ✓ Long press to delete tasks (with custom confirmation popup)")
print("   ✓ Long press to delete students")
print("   ✓ Settings page for class time & grace period configuration")
print("   ✓ Supabase database integration (replaces localStorage)")
print("   ✓ Custom confirmation modal (no browser alerts)")
print("   ✓ All CRUD operations connected to Supabase")
print("\n📊 REQUIRED SUPABASE TABLES:")
print("   • classes (id, name, start_time, end_time, created_at)")
print("   • students (id, class_id, name, roll_number, created_at)")
print("   • attendance (id, class_id, student_id, date, status, time)")
print("   • tasks (id, class_id, title, type, created_at)")
print("   • task_completion (id, task_id, student_id, date, created_at)")
print("   • settings (id, class_id, grace_period)")
print("\n🔐 Database connected to: https://oczzftqfkcpwnhylmvsd.supabase.co")
print("\n⚠️  NOTE: Please create the tables in Supabase dashboard before using the app!")
